import requests
from bs4 import BeautifulSoup
from .utils import setup_logger

logger = setup_logger()

BASE_URL = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page={}"

def fetch_page(page):
    try:
        url = BASE_URL.format(page)
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching page {page}: {e}")
        return None


def parse_listings(html):
    soup = BeautifulSoup(html, "html.parser")
    listings = soup.find_all("div", class_="thumbnail")

    properties = []

    for item in listings:
        try:
            title = item.find("a", class_="title")
            price = item.find("h4", class_="price")
            description = item.find("p", class_="description")

            properties.append({
                "Title": title.get_text(strip=True) if title else "N/A",
                "Price": price.get_text(strip=True) if price else "N/A",
                "Description": description.get_text(strip=True) if description else "N/A"
            })
        except Exception as e:
            logger.error(f"Parsing error: {e}")

    return properties