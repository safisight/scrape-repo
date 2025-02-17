import requests
from bs4 import BeautifulSoup
import csv
import time
from scraperapi_sdk import ScraperAPIClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve API key from .env
api_key = os.getenv("SCRAPERAPI_KEY")

# Initialize ScraperAPI client
scraperapi_client = ScraperAPIClient(api_key)

# Category URL to scrape
category_url = "https://www.jumia.ug/phones-tablets/?page="  # categories
base_url = "https://www.jumia.ug"  # To construct relative links

def scrape_all_products():
    products = []
    page = 1
    while True:
        print(f"Scraping page {page}...")

        # Construct the URL with the page number
        current_page_url = f"{category_url}{page}"

        try:
            # Use ScraperAPI to send requests
            response = scraperapi_client.get(current_page_url)

            # Check if response is a string (HTML content)
            if isinstance(response, str):
                print(f"Received response as string for page {page}")
                response = requests.get(current_page_url)

            if response.status_code != 200:
                print(f"Failed to fetch page {page}. Status code: {response.status_code}")
                break

            # Parse the HTML content
            soup = BeautifulSoup(response.content, "html.parser")

            # Extract product data
            items = soup.find_all("article", class_="prd _fb col c-prd")
            if not items:  # Stop if no products are found
                print("No more products found.")
                break

            for item in items:
                name = item.find("h3", class_="name").get_text(strip=True) if item.find("h3", class_="name") else None
                price = item.find("div", class_="prc").get_text(strip=True) if item.find("div", class_="prc") else None
                link = item.find("a", href=True)["href"] if item.find("a", href=True) else None
                if link:
                    link = f"{base_url}{link}"
                products.append({"Name": name, "Price": price, "Link": link})

            print(f"Found {len(items)} products on page {page}")
            page += 1
            time.sleep(1)  # Wait before scraping the next page

        except requests.exceptions.RequestException as e:
            print(f"Error while scraping page {page}: {e}")
            break

    return products

def save_products_to_csv(products, filename="scraped_products.csv"):
    # Define CSV file header
    header = ["Name", "Price", "Link"]
    
    # Write products data to CSV
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        writer.writerows(products)
    print(f"Scraping complete. Data saved to '{filename}'.")

# Main script execution
if __name__ == "__main__":
    print("Extracting products from the website...")
    all_products = scrape_all_products()
    if all_products:
        save_products_to_csv(all_products)
    else:
        print("No products were scraped.")
