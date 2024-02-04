import os
from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/books', methods=['GET', 'POST'])
def index():
    # Call the books API with parameters
    service_url = os.getenv('API_URL')

    if request.method == 'POST':
        # Extract data from form
        genre = request.form.get('genre')
        author = request.form.get('author')
        title = request.form.get('title')
        
        params = {'genre': genre, 'author': author, 'title': title}
        response = requests.get(service_url, params=params)
        books_response = response.json()

        return render_template('index.html', books=books_response, params=params)

    else:
        # Get query parameters
        genre = request.args.get('genre')
        author = request.args.get('author')
        title = request.args.get('title')
        
        params = {'genre': genre, 'author': author, 'title': title}
        response = requests.get(service_url, params=params)
        books_response = response.json()
        
        return render_template('index.html', books=books_response, params=params)

if __name__ == '__main__':
    app.run(debug=True)

# from flask import Flask, request, jsonify
# from books import get_books

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return """
#     <!DOCTYPE html>
#     <html>
#     <head>
#         <title>Book API</title>
#         <style>
#             body {
#                 background-color: #f0f0f0;
#                 font-family: Arial, sans-serif;
#                 text-align: center;
#             }
#             h1 {
#                 color: #333;
#             }
#             p {
#                 color: #555;
#             }
#         </style>
#     </head>
#     <body>
#         <h1>Welcome to the Book API!</h1>
#         <p>Explore our books <a href="/books">here</a></p>
#     </body>
#     </html>
#     """

# @app.route("/books")
# def books_route():
#     book_id = request.args.get('id')
#     genre = request.args.get('genre')

#     try:
#         filtered_books = get_books(book_id, genre)
#         return jsonify(filtered_books)
#     except ValueError as e:
#         return str(e), 400

# if __name__ == '__main__':
#     app.run(debug=True)

