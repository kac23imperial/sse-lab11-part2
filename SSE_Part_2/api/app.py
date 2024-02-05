import os
from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/books', methods=['GET', 'POST'])
def index():
    # Call the books API with parameters
    service_url = os.getenv('API_URL')
    if not service_url:
        return "API URL not configured", 500

    # Adjusted to only use 'id' and 'genre'
    genre = request.values.get('genre')  # Works for both GET and POST
    book_id = request.values.get('id')  # Fetch 'id' parameter

    # Updated params to include only 'id' and 'genre'
    params = {'genre': genre, 'id': book_id}
    
    try:
        response = requests.get(service_url, params=params)
        if response.status_code == 200:
            books_response = response.json()
            return render_template('index.html', books=books_response, params=params)
        else:
            return f"Failed to fetch books. API responded with status code: {response.status_code}", 502
    except requests.exceptions.RequestException as e:
        return f"API request failed: {e}", 500

if __name__ == '__main__':
    app.run(debug=True)