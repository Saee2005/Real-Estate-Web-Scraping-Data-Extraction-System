from scraper.scraper import fetch_page, parse_listings
from scraper.cleaner import clean_data
import pandas as pd
import os
import time

def main():
    all_properties = []

    for page in range(1, 6):  # Pagination
        print(f"Scraping Page {page}...")
        html = fetch_page(page)

        if html:
            listings = parse_listings(html)
            all_properties.extend(listings)

        time.sleep(1)

    df = clean_data(all_properties)

    os.makedirs("data", exist_ok=True)
    df.to_csv("data/properties.csv", index=False)

    print("\nScraping Completed Successfully!")
    print("Total Listings:", len(df))


if __name__ == "__main__":
    main()