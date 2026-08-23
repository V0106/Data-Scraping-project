# Data Scraping Project Presentation

**Author:** [Your name]  
**Presentation date:** 2026-08-23

## Slide 1: Title

- Data Scraping Project
- Your name
- Presentation date

## Slide 2: Project Objectives

- Collect data from practice websites.
- Parse useful fields from HTML pages.
- Save clean data as CSV files.

## Slide 3: Technologies

- Python
- `requests`
- `BeautifulSoup`
- `pandas`

## Slide 4: Quote Scraper

- Website: Quotes to Scrape
- Fields: quote and author
- Output: `quotes.csv`

## Slide 5: Book Scraper

- Website: Books to Scrape
- Fields: title, price, rating, availability, and book URL
- Output: `book_scraper/book_scraper.csv`

## Slide 6: E-Commerce Scraper

- Website: Webscraper.io test site
- Fields: product name, price, and description
- Output: `ecommerce_scrapper/products.csv`

## Slide 7: Workflow

1. Send a request to the website.
2. Parse the HTML response.
3. Select the required elements.
4. Build structured records.
5. Export the records to CSV.

## Slide 8: Results

The current output contains:

| CSV file | Records | Sample |
|---|---:|---|
| `quotes.csv` | 10 | Quote by Albert Einstein |
| `book_scraper/book_scraper.csv` | 20 | A Light in the Attic, £51.77 |
| `ecommerce_scrapper/products.csv` | 3 | Asus ROG STRIX GL553VD-DM256, $899 |

Add screenshots or sample rows from:

- `quotes.csv`
- `book_scraper/book_scraper.csv`
- `ecommerce_scrapper/products.csv`

## Slide 9: Challenges and Improvements

- Websites may change their HTML structure.
- Requests can fail or return incomplete data.
- Future work could add error handling, pagination, timeouts, and automated tests.

## Slide 10: Work Log and Summary

| Date | Hours | Work completed |
|---|---:|---|
| 2026-08-05 | 3 hours | Created the project from scratch and learned the initial quote scraper. |
| 2026-08-22 | 5 hours | Added the book and e-commerce scrapers. |
| 2026-08-23 | 2 hours | Prepared the report and presentation outline. |

**Summary:** The project demonstrates how Python can collect web data, extract meaningful fields, and save the results for later use.
