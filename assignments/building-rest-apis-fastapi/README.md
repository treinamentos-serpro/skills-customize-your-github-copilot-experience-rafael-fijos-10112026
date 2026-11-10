# 📘 Atividade: Building REST APIs with FastAPI

## 🎯 Objetivo

Construa uma API REST para consultar e gerenciar uma coleção de livros usando FastAPI. Você praticará rotas HTTP, validação de dados com modelos Pydantic e respostas com códigos de status apropriados.

## 📝 Tarefas

### 🛠️ Criar a aplicação e consultar livros

#### Descrição
Complete o starter code para criar uma aplicação FastAPI e implementar endpoints que listem os livros e consultem um livro pelo seu ID.

Instale as dependências e inicie a aplicação com:

```bash
pip install fastapi uvicorn
uvicorn starter-code:app --reload
```

Use `http://127.0.0.1:8000/docs` para testar os endpoints pela documentação interativa do FastAPI.

#### Requisitos
O programa concluído deve:

- Criar uma aplicação FastAPI chamada `app`.
- Implementar `GET /books` para retornar todos os livros da coleção em memória.
- Implementar `GET /books/{book_id}` para retornar um livro pelo ID.
- Retornar o status HTTP `404` quando o ID solicitado não existir.

### 🛠️ Adicionar e remover livros

#### Descrição
Amplie a API para aceitar novos livros e removê-los pelo ID. Use o modelo de entrada fornecido para validar os dados e mantenha as alterações na coleção em memória enquanto a aplicação estiver em execução.

#### Requisitos
O programa concluído deve:

- Implementar `POST /books` para criar um livro com título, autor e ano de publicação válidos.
- Atribuir um ID único ao novo livro e retornar o livro criado com status HTTP `201`.
- Implementar `DELETE /books/{book_id}` para remover um livro existente e retornar status HTTP `204`.
- Retornar status HTTP `404` ao tentar remover um livro que não existe.
- Usar validação do Pydantic para rejeitar dados de entrada inválidos.