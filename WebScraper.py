from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
import csv

app = Flask(__name__)

def scrape_headlines(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        # Generic extraction
        headlines = soup.find_all(['h1', 'h2', 'h3'])

        data = []
        for tag in headlines:
            text = tag.get_text(strip=True)
            if text:
                data.append(text)

        return data

    except Exception as e:
        return {"error": str(e)}


def save_to_csv(data):
    with open("headlines.csv", "w", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Headline"])
        for item in data:
            writer.writerow([item])


# ✅ POST API
@app.route('/scrape', methods=['POST'])
def scrape_api():
    body = request.get_json()

    if not body or 'url' not in body:
        return jsonify({"error": "Missing 'url' in request body"}), 400

    url = body['url']

    data = scrape_headlines(url)

    if isinstance(data, dict) and "error" in data:
        return jsonify(data), 500

    save_to_csv(data)

    return jsonify({
        "message": "Scraping successful",
        "url": url,
        "total_items": len(data),
        "data": data
    })


if __name__ == "__main__":
    app.run(debug=True)