from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Logging
logging.basicConfig(level=logging.INFO)

books = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "Sapiens", "author": "Yuval Noah Harari"}
]

@app.route("/books", methods=["GET"])
def get_books():
    logging.info("Fetching all books")
    return jsonify(books)

@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if not book:
        logging.warning(f"Book {book_id} not found")
        return jsonify({"error": "Not found"}), 404
    return jsonify(book)

@app.route("/books", methods=["POST"])
def add_book():
    data = request.json
    new_book = {"id": len(books) + 1, "title": data["title"], "author": data["author"]}
    books.append(new_book)
    logging.info(f"Added book: {new_book}")
    return jsonify(new_book), 201

@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    global books
    books = [b for b in books if b["id"] != book_id]
    logging.info(f"Deleted book {book_id}")
    return jsonify({"message": "Deleted"})
