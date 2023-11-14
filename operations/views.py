from django.shortcuts import render, redirect
from .models import Book
from .forms import BookCreate
from django.http import HttpResponse

# Create your views here.

def index(request):
    shelf = Book.objects.all()
    return render(request, 'book/book.html',{'shelf': shelf})

#upload
def Upload_book(request):
    upload = BookCreate()
    if request.method == 'POST':
        upload = BookCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""Something went wrong.  please reload the page by clicking <a href="{{url: 'index'}}>Reload</a>" """)
    
    else:
        return render(request, 'book/upload_form.html',{"upload_form": upload})

#update
def update_book(request, book_id):
    book_id = int(book_id)
    try:
        book_shelf = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        return redirect('index')
    book_form = BookCreate(request.POST or None, instance = book_shelf)
    if book_form.is_valid():
        book_form.save()
        return redirect('index')
    return render(request, 'book/upload_form.html', {"upload_form": book_form})

#delete
def delete_book(request, book_id):
    book_id = int(book_id)
    try:
        book_shelf = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        return redirect('index')
    book_shelf.delete()
    return redirect('index')