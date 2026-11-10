# 📘 Assignment: SQLite Persistence with FastAPI

## 🎯 Objective

Extend a FastAPI application to store books in a SQLite database instead of an in-memory collection. By the end, the application should retain its data after a restart and continue handling book queries and creation correctly.

## 📝 Tasks

### 🛠️ Create the database and books table

#### Descrição
Set up the SQLite database using Python's built-in `sqlite3` module. The application should prepare the table automatically when it starts.

#### Requisitos
The completed program must:

- Create the `books.db` file in the same directory as the starter code.
- Create a `books` table if it does not already exist, with an auto-incrementing integer `id` and required `title`, `author`, and `published_year` fields.
- Initialize the database during the FastAPI application's lifespan.

### 🛠️ Persist and query books through the API

#### Descrição
Replace the in-memory storage with queries to the `books` table. Start the application and use FastAPI's interactive documentation to test the endpoints.

Install the dependencies and start the application with:

```bash
pip install fastapi uvicorn
uvicorn starter-code:app --reload
```

Visit `http://127.0.0.1:8000/docs` to test the API.

#### Requisitos
The completed program must:

- Implement `GET /books` to list the stored books.
- Implement `GET /books/{book_id}` to retrieve a book by ID and return HTTP status `404` when it does not exist.
- Implement `POST /books` to insert a book and return the created record with HTTP status `201`.
- Use SQL placeholders (`?`) in queries that include user-provided values.
- Create a book, restart the application, and confirm that the book is still stored.
