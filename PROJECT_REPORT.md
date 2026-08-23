# Data Scraping Project Report

**Author:** [Your name]  
**Date:** 2026-08-23  
**Version:** 1.0

## 1. Introduction

This project uses Python to collect structured information from practice websites and save the results as CSV files.

## 2. Objectives

- Extract quotes and authors.
- Extract book details such as title, price, rating, availability, and URL.
- Extract e-commerce product names, prices, and descriptions.
- Store the collected information in reusable CSV files.

## 3. Tools Used

- Python
- `requests` for downloading web pages
- `BeautifulSoup` for parsing HTML
- `pandas` for creating CSV files

## 4. Scrapers and Outputs

| Scraper | Website | Data collected | Output |
|---|---|---|---|
| `scraper.py` | Quotes to Scrape | Quote and author | `quotes.csv` |
| `book_scraper/book_scraper.py` | Books to Scrape | Title, price, rating, availability, URL | `book_scraper/book_scraper.csv` |
| `ecommerce_scrapper/escaper.py` | Webscraper.io test site | Product, price, description | `ecommerce_scrapper/products.csv` |

## 5. Implementation Summary

Each scraper sends an HTTP request, parses the returned HTML, selects the required elements, builds a list of records, and writes the records to a CSV file with pandas.

## 6. Actual Results

The CSV files currently contain the following data:

| Output file | Records | Example data |
|---|---:|---|
| `quotes.csv` | 10 | Albert Einstein - “The world as we have created it...” |
| `book_scraper/book_scraper.csv` | 20 | A Light in the Attic - £51.77 - Three - In stock |
| `ecommerce_scrapper/products.csv` | 3 | Asus ROG STRIX GL553VD-DM256 - $899 |

Sample extracted fields:

- Quote: `The world as we have created it is a process of our thinking.`
- Book: `A Light in the Attic`, price `£51.77`, rating `Three`, availability `In stock`.
- Product: `Asus ROG STRIX GL553VD-DM256`, price `$899`.

## 7. How to Run

Install the dependencies:

```powershell
python -m pip install requests beautifulsoup4 pandas
```

Run the scrapers from the project folder:

```powershell
python scraper.py
python book_scraper\book_scraper.py
python ecommerce_scrapper\escaper.py
```

## 8. Validation

The scripts print the website status or completion message and confirm that data was saved to the expected CSV file.

## 9. Limitations and Improvements

- Add request timeouts to every scraper.
- Add error handling for failed requests and missing HTML elements.
- Add pagination support for larger websites.
- Respect website terms of use and rate limits.
- Add automated tests for the extracted fields.

## 10. Work Log

The hours below are beginner-friendly estimates for work completed from scratch.

| Date | Hours | Work completed | Deliverable |
|---|---:|---|---|
| 2026-08-05 | 3 hours | Created the project from scratch and learned the initial quote scraper. | `scraper.py`, `quotes.csv` |
| 2026-08-22 | 3 hours | Created the book scraper. | `book_scraper/book_scraper.py`, `book_scraper/book_scraper.csv` |
| 2026-08-22 | 2 hours | Created the e-commerce scraper. | `ecommerce_scrapper/escaper.py`, `ecommerce_scrapper/products.csv` |
| 2026-08-23 | 2 hours | Prepared the project report and presentation outline. | `PROJECT_REPORT.md`, `PRESENTATION_OUTLINE.md` |
