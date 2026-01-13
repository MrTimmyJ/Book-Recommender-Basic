# Book Recommender Basic

A simple Flask application that uses the Google Books API to recommend similar books based on a query.

**Author**: Timothy Johnson<br>
**Date**: January 2026

## Overview
Book Recommender Basic is a lightweight Flask application that provides book recommendations by querying the Google Books API. It searches for books similar to a given title and returns formatted recommendations through a simple web interface.

## ✨ Features

### 🔍 Smart Book Search
- **Enhanced Query Processing**: Searches for "books like [query]" instead of exact matches
- **Intelligent Filtering**: Automatically excludes the exact book from search results
- **Results Curation**: Returns up to 10 relevant similar books

### 📚 Structured Book Information
- **Comprehensive Data**: Extracts titles, authors, categories, and descriptions
- **Formatted Output**: Presents clean, readable book information
- **Description Snippets**: Provides concise 100-character book descriptions

### 🔌 API Endpoints
- **Interactive Homepage**: Web interface with test links
- **Test Endpoint**: GET endpoint for quick testing
- **Recommendation Endpoint**: POST endpoint for structured recommendations

## 🧰 Technologies Used

### 🌐 Backend Framework
- **Flask** - Python web framework
- **Requests** - HTTP library for API calls

### 📊 External APIs
- **Google Books API** - Book search and metadata

### 🎨 Frontend & UI
- **HTML5** - Web page structure
- **Flask Templating** - Dynamic content rendering

### 🔧 Development Tools
- **Python 3** - Programming language
- **JSON** - Data interchange format

## 📊 API Endpoints

| Endpoint | Method | Description | Parameters |
|----------|--------|-------------|------------|
| `/` | GET | Homepage with test links | None |
| `/test` | GET | Test book search | `book` (query parameter) |
| `/recommend` | POST | Get book recommendations | JSON: `{"book": "Book Title"}` |

## 🆚 How It Works

| Step | Process | Example |
|------|---------|---------|
| 1. Input | User provides a book title | "Harry Potter" |
| 2. Query Enhancement | Converts to "books like [title]" | "books like Harry Potter" |
| 3. API Search | Searches Google Books API | Returns 15 initial results |
| 4. Filtering | Removes exact matches | Filters out "Harry Potter" books |
| 5. Recommendation | Selects specific results | Top pick, genre variations |

## 📁 Code Structure
book-recommender-basic/<br>
├── app.py # Main Flask application<br>
├── requirements.txt # Python dependencies<br>
└── README.md # Project documentation<br>


## 🚀 Getting Started

### Prerequisites
- Python 3.6+
- Flask
- Requests library

### Installation

1. Clone and setup:

    git clone https://github.com/MrTimmyJ/book-recommender-basic.git <br>
    cd book-recommender-basic

2. Install dependencies:

    Create and activate virtual environment
    
    python3 -m venv venv<br>
    source venv/bin/activate  # Mac/Linux<br>
    venv\Scripts\activate   # Windows

    Install Flask
    
    pip install flask requests

3. Run application:

     python app.py

🪪 License

© 2026 Timothy Johnson. All Rights Reserved.<br>
This project and its code may not be copied, modified, or reused without permission.
