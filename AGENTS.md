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

When creating presentation slides, include:

- Project title, author, and presentation date.
- Problem statement and project objectives.
- Websites and data fields collected.
- Tools used: Python, `requests`, `BeautifulSoup`, and `pandas`.
- A short explanation of each scraper's workflow.
- Screenshots or sample rows from each generated CSV file.
- Results, challenges, and possible improvements.
- A final summary of the work completed and total hours spent.

Suggested slide activity record:

| Date | Hours | Slides completed | Notes |
|---|---:|---|---|
| 2026-08-23 | 1 hour | Planned the presentation slides and added project results. | `PRESENTATION_OUTLINE.md` | Complete |

## Documents

When creating project documents or reports, include:

- Project title, author, date, and version.
- Introduction, objectives, and scope.
- Scraper design and implementation details.
- Installation and execution instructions.
- Source websites and fields extracted.
- Output file names and sample results.
- Testing or validation performed.
- Limitations, ethical considerations, and future improvements.
- A dated work log with hours and completed tasks.

Current project documents:

- `PROJECT_REPORT.md` - project report with implementation details and work log.
- `PRESENTATION_OUTLINE.md` - slide-by-slide presentation content and work log.

Suggested document activity record:

| Date | Hours | Document section completed | Notes |
|---|---:|---|---|
| 2026-08-23 | 1 hour | Prepared the project report with results and work log. | `PROJECT_REPORT.md` | Complete |

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
