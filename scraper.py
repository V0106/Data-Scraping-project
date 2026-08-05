import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://quotes.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

quotes = []
authors = []

for quote in soup.find_all("span", class_="text"):
    quotes.append(quote.text)

for author in soup.find_all("small", class_="author"):
    authors.append(author.text)

data = {
    "Quote": quotes,
    "Author": authors
}

df = pd.DataFrame(data)

print(df)

df.to_csv("quotes.csv", index=False)

print("Data saved successfully")