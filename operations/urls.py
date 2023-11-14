from django.urls import path
from . import views
from CRUD.settings import DEBUG, STATIC_ROOT, STATIC_URL, MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.Upload_book, name='Upload-book'),
    path('update/<int:book_id>', views.update_book, name='update'),
    path('delete/<int:book_id>', views.delete_book, name='delete'),
]
if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)
 
 