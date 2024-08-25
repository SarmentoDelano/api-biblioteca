from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Livro
from .serializers import LivroSerializer

@api_view(['GET', 'POST'])
def livro_list_create(request): 
    if request.method == 'GET': 
        livros = Livro.objects.all() 
        serializer = LivroSerializer(livros, many=True) 
        return Response(serializer.data)
    
    elif request.method == 'POST': 
        serializer = LivroSerializer(data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def livro_detail(request, pk): 
    try:
        livro = Livro.objects.get(pk=pk)
    except Livro.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET': 
        serializer = LivroSerializer(livro) 
        return Response(serializer.data)
    
    elif request.method == 'PUT': 
        serializer = LivroSerializer(livro, data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE': 
        livro.delete() 
        return Response(status=status.HTTP_204_NO_CONTENT)
