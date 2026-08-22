import requests
import pandas as pd

from bs4 import BeautifulSoup
from urllib.parse import urljoin


url = "https://books.toscrape.com/"
response = requests.get(url, timeout=30)

print("Website status:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

books = []

book_cards = soup.select("article.product_pod")

for card in book_cards:
    title_tag = card.select_one("h3 a")
    price_tag = card.select_one(".price_color")
    rating_tag = card.select_one("p.star-rating")
    availability_tag = card.select_one(".availability")

    title = title_tag.get("title")
    price = price_tag.get_text(strip=True)
    rating = " ".join(rating_tag.get("class", []))
    availability = availability_tag.get_text(" ", strip=True)

    book_url = urljoin(url, title_tag.get("href"))

    books.append({
        "title": title,
        "price": price,
        "rating": rating,
        "availability": availability,
        "book_url": book_url
    })

dataframe = pd.DataFrame(books)

dataframe.to_csv("book_scraper.csv", index=False)

print("Scraping finished")
print("Books found:", len(books))
print("Saved file: book_scraper.csv")