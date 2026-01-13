from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

def search_google_books(query):
    """Search for books similar to the query, not just the query itself"""
    print(f"🔍 Searching for books like: {query}")
    
    # Enhanced search - look for similar books, not exact matches
    enhanced_query = f"books like {query}"
    
    url = "https://www.googleapis.com/books/v1/volumes"
    params = {
        'q': enhanced_query,
        'maxResults': 15
    }
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        items = data.get('items', [])
        
        # Filter out the exact same book
        filtered_items = [
            item for item in items 
            if query.lower() not in item.get('volumeInfo', {}).get('title', '').lower()
        ][:10]  # Take first 10 that aren't the exact book
        
        print(f"✅ Found {len(filtered_items)} similar books")
        return filtered_items
    except Exception as e:
        print(f"❌ Error: {e}")
        return []

# def search_google_books(query):
#     """Search Google Books API"""
#     print(f"🔍 Searching for: {query}")
    
#     url = "https://www.googleapis.com/books/v1/volumes"
#     params = {
#         'q': query,
#         'maxResults': 10
#     }
    
#     try:
#         response = requests.get(url, params=params)
#         data = response.json()
#         print(f"✅ Found {len(data.get('items', []))} results")
#         return data.get('items', [])
#     except Exception as e:
#         print(f"❌ Error: {e}")
#         return []

def format_book(book_item):
    """Extract basic book info"""
    volume_info = book_item.get('volumeInfo', {})
    return {
        'title': volume_info.get('title', 'Unknown'),
        'authors': volume_info.get('authors', ['Unknown']),
        'categories': volume_info.get('categories', ['Unknown']),
        'description': volume_info.get('description', '')[:100] + '...' if volume_info.get('description') else 'No description'
    }

@app.route('/test', methods=['GET'])
def test_recommendation():
    """Test endpoint to see what Google returns"""
    book_title = request.args.get('book', 'Harry Potter')
    
    print(f"\n🎯 Testing with: '{book_title}'")
    results = search_google_books(book_title)
    
    if not results:
        return jsonify({"error": "No books found", "tested_with": book_title})
    
    books = [format_book(item) for item in results]
    
    response = {
        "tested_with": book_title,
        "total_found": len(books),
        "results": books
    }
    
    print(f"📚 Sample results:")
    for i, book in enumerate(books[:3]):
        print(f"  {i+1}. {book['title']} by {book['authors'][0]}")
    
    return jsonify(response)

@app.route('/recommend', methods=['POST'])
def simple_recommend():
    """Basic recommendation endpoint"""
    data = request.get_json()
    user_book = data.get('book', 'Harry Potter').strip()
    
    results = search_google_books(user_book)
    
    if not results:
        return jsonify({"error": "No books found. Try another title."})
    
    books = [format_book(item) for item in results]
    
    # Simple recommendation logic
    if len(books) >= 3:
        recommendations = {
            "top_pick": books[0],
            "same_genre_different_style": books[2], 
            "different_genre_same_vibes": books[4] if len(books) > 4 else books[1]
        }
    else:
        recommendations = {"error": "Not enough books found"}
    
    return jsonify(recommendations)

@app.route('/')
def home():
    return """
    <h1>Book Recommender Test</h1>
    <p>Test endpoints:</p>
    <ul>
        <li><a href="/test?book=Harry+Potter">/test?book=Harry+Potter</a></li>
        <li><a href="/test?book=Dune">/test?book=Dune</a></li>
        <li><a href="/test?book=The+Hobbit">/test?book=The+Hobbit</a></li>
    </ul>
    <p>Use POST to /recommend with JSON: {"book": "Book Title"}</p>
    """

if __name__ == '__main__':
    print("🚀 Starting Book Recommender Test...")
    print("📖 Open: http://localhost:5000")
    print("🔍 Test with: http://localhost:5000/test?book=Harry+Potter")
    app.run(debug=True, port=5000)
