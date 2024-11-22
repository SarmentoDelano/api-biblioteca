from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from . import views

urlpatterns = [
    path('livros/', views.LivroList.as_view(), name='livros-list'),
    path('livros/<int:pk>/', views.LivroDetail.as_view(), name='livro-detail'),
    path('autor/', views.AutorList.as_view(), name='autor-list'),
    path('categoria/', views.CategoriaList.as_view(), name='categoria-list'),
    path('colecoes/', views.ColecaoListCreate.as_view(), name='colecoes-list-create'),
    path('colecoes/<int:pk>/', views.ColecaoDetail.as_view(), name='colecao-detail'),
    path('api/token-auth/', obtain_auth_token, name='token-auth'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
