from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from .models import Categoria, Autor, Livro, Colecao
from .serializers import LivroSerializer, AutorSerializer, CategoriaSerializer, ColecaoSerializer
from .custom_permissions import IsColecionador


class LivroList(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    filterset_fields = ['titulo', 'autor', 'categoria']
    search_fields = ['^titulo']
    ordering_fields = ['titulo', 'publicado_em']


class LivroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer


class AutorList(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    search_fields = ['^nome']
    ordering_fields = ['nome']


class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    search_fields = ['^nome']
    ordering_fields = ['nome']


class ColecaoListCreate(generics.ListCreateAPIView):
    serializer_class = ColecaoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(colecionador=self.request.user)

    def get_queryset(self):
        return Colecao.objects.filter(colecionador=self.request.user)



class ColecaoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Colecao.objects.all()
    serializer_class = ColecaoSerializer
    permission_classes = [permissions.IsAuthenticated, IsColecionador]
