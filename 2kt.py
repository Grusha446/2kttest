import csv
from csv import DictReader
import json

books = []
with open('books.csv', newline='') as f:
    reader = DictReader(f)
    for row in reader:
        book = {
            "title": row.get("Title"),
            "author": row.get("Author"),
            "pages": row.get("Pages"),
            "genre": row.get("Genre")
        }
        books.append(book)

with open('users.json', "r") as j:
    users = json.loads(j.read())
    num_users = len(users)
    num_books = len(books)
    one_user_book = num_books // num_users
    one_user_remaining_books = num_books % num_users

result = []
for user in users:
    user_books = []
    for i in range(one_user_book):
        if books:
            book = books.pop(0)
            user_books.append({
                "Title": book.get("title"),
                "Author": book.get("author"),
                "Pages": book.get("pages"),
                "Genre": book.get("genre")
            })
    if one_user_remaining_books > 0 and books:
        book = books.pop(0)
        user_books.append({
            "Title": book.get("title"),
            "Author": book.get("author"),
            "Pages": book.get("pages"),
            "Genre": book.get("genre")
        })
        one_user_remaining_books -= 1

    result.append({
        "name": user.get("name"),
        "gender": user.get("gender"),
        "address": user.get("address"),
        "age": user.get("age"),
        "books": user_books
    })


with open("reference.json", 'w') as f:
    json.dump(result, f, indent=4)


