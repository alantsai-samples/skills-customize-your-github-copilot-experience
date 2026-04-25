from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Book(BaseModel):
    id: int
    title: str
    author: str
    year: Optional[int] = None

books: List[Book] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Books API!"}

@app.post("/books", response_model=Book, status_code=201)
def create_book(book: Book):
    for b in books:
        if b.id == book.id:
            raise HTTPException(status_code=422, detail="Book with this ID already exists.")
    books.append(book)
    return book

@app.get("/books", response_model=List[Book])
def get_books():
    return books

@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found.")

@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, updated_book: Book):
    for idx, book in enumerate(books):
        if book.id == book_id:
            books[idx] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found.")

@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int):
    for idx, book in enumerate(books):
        if book.id == book_id:
            del books[idx]
            return
    raise HTTPException(status_code=404, detail="Book not found.")
