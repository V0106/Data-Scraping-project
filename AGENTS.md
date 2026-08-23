# Project Instructions

## Project Activity Log

This project was created from scratch by a beginner. The hours below are reasonable estimates and can be adjusted if needed.

| Date | Hours | Work completed | Deliverable | Status |
|---|---:|---|---|---|
| 2026-08-05 | 3 hours | Created the project from scratch and learned how to build the quote scraper. | `scraper.py`, `quotes.csv` | Complete |
| 2026-08-22 | 3 hours | Added a scraper for book titles, prices, ratings, availability, and URLs. | `book_scraper/book_scraper.py`, `book_scraper/book_scraper.csv` | Complete |
| 2026-08-22 | 2 hours | Added an e-commerce scraper for product names, prices, and descriptions. | `ecommerce_scrapper/escaper.py`, `ecommerce_scrapper/products.csv` | Complete |
| 2026-08-22 | 1 hour | Documented project setup, run commands, outputs, and security guidelines. | `README.md`, `AGENTS.md` | Complete |

## Slides

Presentation content:

- **Slide 1 - Title:** Data Scraping Project, Vaishnavi Padmawar, and presentation date 2026-08-23.
- **Slide 2 - Objectives:** Collect website data, parse HTML, and save clean CSV files.
- **Slide 3 - Technologies Used:** Four equal rounded shapes in a 2x2 layout: Python, `requests`, `BeautifulSoup`, and `pandas`. Each shape is 5.7 x 2.2 inches and all shapes are inside the slide boundaries.
- **Slide 4 - Quote scraper:** Quotes to Scrape; quote and author; output `quotes.csv`.
- **Slide 5 - Book scraper:** Books to Scrape; title, price, rating, availability, and URL; output `book_scraper/book_scraper.csv`.
- **Slide 6 - E-commerce scraper:** Webscraper.io test site; product, price, and description; output `ecommerce_scrapper/products.csv`.
- **Slide 7 - Workflow:** Request the page, parse HTML, select fields, build records, and export CSV.
- **Slide 8 - Results:** Show screenshots or sample rows from each CSV file.
- **Slide 9 - Improvements:** Add error handling, pagination, timeouts, and automated tests.
- **Slide 10 - Summary:** Explain the completed work and total hours.

Suggested slide activity record:

| Date | Hours | Slides completed | Notes |
|---|---:|---|---|
| 2026-08-23 | 1 hour | Planned the presentation slides and added project results. | Slides recorded in this file. | Complete |

All presentation content is recorded in this file; no separate presentation file is required.

## Documents

Project report content:

- Project title, author, date, and version.
- Introduction, objectives, and scope.
- Scraper design and implementation details.
- Installation and execution instructions.
- Source websites and fields extracted.
- Output file names and sample results.
- Testing or validation performed.
- Limitations, ethical considerations, and future improvements.
- **Title:** Data Scraping Project.
- **Author:** Vaishnavi Padmawar.
- **Date:** 2026-08-23.
- **Version:** 1.0.
- **Introduction:** This project uses Python to collect structured information from practice websites and save the results as CSV files.
- **Objectives:** Extract quotes, book details, and e-commerce product details, then store them in CSV files.
- **Implementation:** Each scraper sends an HTTP request, parses HTML, selects the required fields, creates records, and writes them with pandas.
- **Validation:** Scripts print a website status or completion message and confirm that data was saved.
- **Limitations:** Add error handling, timeouts, pagination, and automated tests in future work. Respect website terms and rate limits.

Actual results:

| Output file | Records | Sample |
|---|---:|---|
| `quotes.csv` | 10 | Quote by Albert Einstein |
| `book_scraper/book_scraper.csv` | 20 | A Light in the Attic, £51.77, Three, In stock |
| `ecommerce_scrapper/products.csv` | 3 | Asus ROG STRIX GL553VD-DM256, $899 |

Suggested document activity record:

| Date | Hours | Document section completed | Notes |
|---|---:|---|---|
| 2026-08-23 | 1 hour | Prepared the project report with results and work log. | Report recorded in this file. | Complete |

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
