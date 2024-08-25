from django.urls import path
from . import views

urlpatterns = [
    path('', views.livro_list_create, name='livros-list-create'), 
    path('<int:pk>/', views.livro_detail, name='livro-detail'), 
]
