from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel, Field

app = FastAPI()


class BookCreate(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    published_year: int = Field(ge=1)


class Book(BookCreate):
    id: int


books = [
    {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien", "published_year": 1937},
    {"id": 2, "title": "Frankenstein", "author": "Mary Shelley", "published_year": 1818},
]


# Task 1: Implement the read endpoints.
@app.get("/books", response_model=list[Book])
def get_books():
    pass


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    pass


# Task 2: Implement the create and delete endpoints.
@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book_data: BookCreate):
    pass


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    pass