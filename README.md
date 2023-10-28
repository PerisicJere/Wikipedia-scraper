# Wikipedia Scraper

This Python script is designed to scrape Wikipedia pages, extract links, and information from those pages. It provides the option to scrape either a list from a Wikipedia page or the "See also" section of a Wikipedia page. The extracted data is then written to a CSV file.

### Prerequisites

Before running the script, ensure that you have the following prerequisites installed:

- Required Python packages (You can install them using pip):
  - `beautifulsoup4`
  - `requests`
  - `wikipedia`

You can install the required packages by running the following command:

```bash
pip3 install beautifulsoup4 requests wikipedia
```
### Usage
- Run the program using
```bash
python3 wikipedia_scraper.py
```
- The script will prompt you to choose between scraping a list (e.g., "List of physics") or the "See also" section of a Wikipedia page.
- Depending on your choice, the script will then prompt you to input the link to the Wikipedia page.
- The script will start scraping and display the progress. Once completed, it will generate a CSV file named 'Physics.csv' containing the extracted data.
- You can find the CSV file in the same directory where the script is located.

### Author
Jere Perisic
