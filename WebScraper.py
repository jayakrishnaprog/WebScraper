import requests
from bs4 import BeautifulSoup
import csv

# Target website (example: BBC News)
URL = "https://www.linkedin.com"

def scrape_headlines():
    try:
        # Send HTTP request
        response = requests.get(URL)
        response.raise_for_status()

        # Parse HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract headlines (BBC uses h3 tags for headlines)
        headlines = soup.find_all('h3')

        data = []

        for headline in headlines:
            text = headline.get_text(strip=True)
            if text:
                data.append([text])

        return data

    except Exception as e:
        print("Error:", e)
        return []


def save_to_csv(data):
    with open("headlines.csv", "w", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Headline"])  # header
        writer.writerows(data)


if __name__ == "__main__":
    scraped_data = scrape_headlines()
    
    if scraped_data:
        save_to_csv(scraped_data)
        print("✅ Data saved to headlines.csv")
    else:
        print("❌ No data scraped")