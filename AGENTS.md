# Project Instructions

## Install dependencies

```powershell
python -m pip install requests beautifulsoup4 pandas
```

## Run the scrapers

From the `Data Scraping` folder:

```powershell
python book_scraper\book_scraper.py
python ecommerce_scrapper\escaper.py
```

## Output files

- `book_scraper\book_scraper.csv`
- `ecommerce_scrapper\products.csv`

## Guidelines

- Keep scraper code simple and readable.
- Use `requests` for downloading pages, `BeautifulSoup` for parsing HTML, and `pandas` for CSV output.
- Do not commit passwords, API keys, or other private information.
