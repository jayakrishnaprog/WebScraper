py webscraper.py
http://localhost:5000/scrape


{
    "data": [
        "Check out Gayatri’s story of finding a new job on LinkedIn",
        "General",
        "Browse LinkedIn",
        "Business Solutions",
        "Directories"
    ],
    "message": "Scraping successful",
    "total_headlines": 5
}


curl -X POST http://localhost:5000/scrape \
-H "Content-Type: application/json" \
-d "{\"url\": \"https://www.bbc.com/news\"}"
