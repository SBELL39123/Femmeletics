# Women's Sports News Aggregator

A Flask web application that aggregates and displays real-time news articles on women's sports. The app integrates with [NewsAPI](https://newsapi.org/) to fetch current news and categorizes content by sports and notable athletes. It also provides links to tickets, merchandise stores, and social media related to women's sports.

## Features

- Dynamic news fetching from NewsAPI with keyword-based filtering for women's sports topics.
- Search functionality with keyword routing to specific sports pages.
- Displays categorized news articles with main and sidebar sections.
- Lists global ticket vendors, merchandise stores, and social media links for various women's sports.
- Secure handling of API keys using environment variables.
- Custom 404 error page for unmatched routes or search terms.

## Technologies Used

- Python 3
- Flask
- Requests
- dotenv for environment variable management
- HTML/CSS (Jinja2 templates)

## Setup Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/womens-sports-news-aggregator.git
    cd womens-sports-news-aggregator
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Obtain a free API key from [NewsAPI](https://newsapi.org/) and create a `.env` file in the project root with:
    ```
    NEWS_API_KEY=your_api_key_here
    ```

5. Run the application:
    ```bash
    flask run
    ```

6. Open your browser and navigate to `http://127.0.0.1:5000`

## Project Structure
/app.py           # Main Flask application
/templates/       # HTML templates (index.html, basketball.html, search_results.html, etc.)
/static/          # CSS, images, JavaScript files (if any)
/.env             # Environment variables file (not committed to repo)
requirements.txt  # Python dependencies
README.md         # This file


## Usage

- Use the search bar to find news by sports or athlete names.
- Navigate to category pages like Basketball, Soccer, Tennis, etc.
- Explore ticket, merchandise, and social media links for women's sports.

## License

This project is licensed under the MIT License.

---


## Acknowledgments 
- NewsAPI for the news data API.
- Inspiration from various women’s sports leagues and communities.