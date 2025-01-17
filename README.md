# **API de Biblioteca**

Uma API desenvolvida com Django REST Framework para gerenciar coleções de livros, autores e categorias, permitindo que usuários criem, atualizem e acessem informações de maneira eficiente.

---

## **Recursos da API**

A API fornece endpoints para:

- Gerenciar **Coleções**:
  - Criar coleções personalizadas de livros.
  - Associar coleções a um colecionador específico (usuário autenticado).
- Gerenciar **Livros**:
  - Criar, visualizar, atualizar e excluir livros.
  - Relacionar livros a autores e categorias.
- Gerenciar **Autores**:
  - Criar, visualizar, atualizar e excluir informações de autores.
- Gerenciar **Categorias**:
  - Criar, visualizar, atualizar e excluir categorias de livros.

---

## **Tecnologias Utilizadas**

- **Python**: Linguagem de programação.
- **Django**: Framework web para back-end.
- **Django REST Framework (DRF)**: Para criação de APIs RESTful.
- **SQLite**: Banco de dados usado no desenvolvimento.

---

## **Configuração do Ambiente**

### **1. Pré-requisitos**
- Python 3.8+
- Pipenv (ou pip para gerenciar pacotes)
- Git
- Banco de dados SQLite

### **2. Clonar o Repositório**
```bash
git clone https://github.com/SarmentoDelano/api-biblioteca.git
cd api-biblioteca
```

### **3. Instalar Dependências**
```bash
pip install -r requirements.txt
```

### **4. Executar Migrações**
```bash
python manage.py makemigrations
python manage.py migrate
```

### **5. Rodar o Servidor**
```bash
python manage.py runserver
```
Acesse a API em `http://127.0.0.1:8000/`.

---

## **Endpoints**

### **Coleções**
| Método | Endpoint           | Descrição                                |
|--------|--------------------|------------------------------------------|
| GET    | /colecoes/         | Lista todas as coleções                 |
| POST   | /colecoes/         | Cria uma nova coleção                   |
| GET    | /colecoes/{id}/    | Recupera detalhes de uma coleção        |
| PUT    | /colecoes/{id}/    | Atualiza uma coleção existente          |
| DELETE | /colecoes/{id}/    | Remove uma coleção                      |

### **Livros**
| Método | Endpoint           | Descrição                                |
|--------|--------------------|------------------------------------------|
| GET    | /livros/           | Lista todos os livros                   |
| POST   | /livros/           | Adiciona um novo livro                  |
| GET    | /livros/{id}/      | Recupera detalhes de um livro           |
| PUT    | /livros/{id}/      | Atualiza informações de um livro        |
| DELETE | /livros/{id}/      | Remove um livro                         |

### **Autores**
| Método | Endpoint           | Descrição                                |
|--------|--------------------|------------------------------------------|
| GET    | /autores/          | Lista todos os autores                  |
| POST   | /autores/          | Adiciona um novo autor                  |
| GET    | /autores/{id}/     | Recupera detalhes de um autor           |
| PUT    | /autores/{id}/     | Atualiza informações de um autor        |
| DELETE | /autores/{id}/     | Remove um autor                         |

### **Categorias**
| Método | Endpoint           | Descrição                                |
|--------|--------------------|------------------------------------------|
| GET    | /categorias/       | Lista todas as categorias               |
| POST   | /categorias/       | Adiciona uma nova categoria             |
| GET    | /categorias/{id}/  | Recupera detalhes de uma categoria      |
| PUT    | /categorias/{id}/  | Atualiza informações de uma categoria   |
| DELETE | /categorias/{id}/  | Remove uma categoria                    |

---
