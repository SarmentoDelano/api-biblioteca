from django.urls import path 
from . import views 

urlpatterns = [ 
    path('livros/', views.LivroList.as_view(), name='livros-list'), 
    path('livros/<int:pk>/', views.LivroDetail.as_view(), name='livro-detail'), 
    path('autor/', views.AutorList.as_view(), name='autor-list'), 
    path('categoria/', views.CategoriaList.as_view(), name='categoria-list'), 
] 
