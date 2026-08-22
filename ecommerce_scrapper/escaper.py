import requests
import pandas as pd

from bs4 import BeautifulSoup


url = "https://webscraper.io/test-sites/e-commerce/allinone"

response = requests.get(url)

print("Website status:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

products = []

product_cards = soup.find_all("div", class_="thumbnail")

for card in product_cards:
    title_tag = card.find("a", class_="title")
    price_tag = card.find("h4", class_="price")
    description_tag = card.find("p", class_="description")

    product_name = title_tag.get("title")
    price = price_tag.get_text(strip=True)
    description = description_tag.get_text(strip=True)

    products.append({
        "Product": product_name,
        "Price": price,
        "Description": description
    })

dataframe = pd.DataFrame(products)

dataframe.to_csv("products.csv", index=False)

print("Scraping finished")
print("Products found:", len(products))
print("Data saved in products.csv")