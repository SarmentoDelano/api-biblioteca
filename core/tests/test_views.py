from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from core.models import Categoria, Autor, Livro, Colecao
from rest_framework.authtoken.models import Token

class ColecaoAPITests(APITestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='password1')
        self.user2 = User.objects.create_user(username='user2', password='password2')

        self.token_user1 = Token.objects.create(user=self.user1)
        self.token_user2 = Token.objects.create(user=self.user2)

        self.categoria = Categoria.objects.create(nome="Ficção")
        self.autor = Autor.objects.create(nome="Autor Teste")

        self.livro1 = Livro.objects.create(
            titulo="Livro 1",
            autor=self.autor,
            categoria=self.categoria,
            publicado_em="2023-01-01"
        )
        self.livro2 = Livro.objects.create(
            titulo="Livro 2",
            autor=self.autor,
            categoria=self.categoria,
            publicado_em="2023-01-02"
        )

        self.colecao1 = Colecao.objects.create(nome="Coleção 1", colecionador=self.user1)
        self.colecao1.livros.set([self.livro1])

        self.colecao2 = Colecao.objects.create(nome="Coleção 2", colecionador=self.user2)
        self.colecao2.livros.set([self.livro2])
        self.client = APIClient()

    def test_criar_colecao_autenticado(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token_user1.key}')
        data = {
            "nome": "Nova Coleção",
            "descricao": "Descrição da coleção",
            "livros": [self.livro1.id]
        }
        response = self.client.post('/colecoes/', data, format='json')

        print("Response data:", response.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Colecao.objects.count(), 3)
        self.assertEqual(Colecao.objects.last().colecionador, self.user1)

    def test_criar_colecao_nao_autenticado(self):
        data = {"nome": "Nova Coleção", "descricao": "Descrição da coleção", "livros": [self.livro1.id]}
        response = self.client.post('/colecoes/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_editar_colecao_propria(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token_user1.key}')
        data = {"nome": "Coleção Atualizada"}
        response = self.client.patch(f'/colecoes/{self.colecao1.id}/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Colecao.objects.get(id=self.colecao1.id).nome, "Coleção Atualizada")

    def test_editar_colecao_outra_pessoa(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token_user1.key}')
        data = {"nome": "Tentativa de Atualização"}
        response = self.client.patch(f'/colecoes/{self.colecao2.id}/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_deletar_colecao_propria(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token_user1.key}')
        response = self.client.delete(f'/colecoes/{self.colecao1.id}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Colecao.objects.filter(id=self.colecao1.id).exists())

    def test_deletar_colecao_outra_pessoa(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token_user1.key}')
        response = self.client.delete(f'/colecoes/{self.colecao2.id}/')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_listar_colecoes_autenticado(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token_user1.key}')
        response = self.client.get('/colecoes/')
        user_colecoes = Colecao.objects.filter(colecionador=self.user1)
        print("Response data:", response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), user_colecoes.count())

        for colecao in response.data['results']:
            self.assertEqual(colecao['colecionador'], self.user1.username)



    def test_listar_colecoes_nao_autenticado(self):
        response = self.client.get('/colecoes/')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    def tearDown(self):
        Colecao.objects.all().delete()
        Livro.objects.all().delete()
        Categoria.objects.all().delete()
        Autor.objects.all().delete()
