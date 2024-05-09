from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory list of books
books = [
    {'id': 1, 'book_name': '1984', 'author': 'George Orwell', 'publisher': 'Secker & Warburg'},
    {'id': 2, 'book_name': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'publisher': 'J. B. Lippincott & Co.'}
]

# CRUD operations

# Create a Book
@app.route('/book', methods=['POST'])
def add_book():
    new_book = {
        'id': books[-1]['id'] + 1,
        'book_name': request.json['book_name'],
        'author': request.json['author'],
        'publisher': request.json['publisher']
    }
    books.append(new_book)
    return jsonify(new_book), 201

# Read all Books
@app.route('/book', methods=['GET'])
def get_books():
    return jsonify(books)

# Read a single Book
@app.route('/book/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    return jsonify(book) if book else ('', 404)

# Update a Book
@app.route('/book/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if not book:
        return '', 404
    book['book_name'] = request.json.get('book_name', book['book_name'])
    book['author'] = request.json.get('author', book['author'])
    book['publisher'] = request.json.get('publisher', book['publisher'])
    return jsonify(book)

# Delete a Book
@app.route('/book/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [b for b in books if b['id'] != book_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
