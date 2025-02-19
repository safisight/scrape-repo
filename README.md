# Products Scraper

This Python script scrapes product information from the Jumia Uganda website, specifically from the Phones & Tablets category. It collects product names, prices, and links to individual product pages, then saves the data to a CSV file.

## Features

Scrapes multiple pages of products from Jumia Uganda's Phones & Tablets category.
Extracts product names, prices, and links.
Saves the scraped data to a CSV file (scraped_products.csv).
Utilizes ScraperAPI to bypass anti-scraping measures.

## Prerequisites

Make sure you have the following installed:

Python 3.x

## Required libraries

requests
beautifulsoup4
csv
time
scraperapi_sdk
python-dotenv

## You can install the required libraries using

```bash
pip install requests beautifulsoup4 scraperapi-sdk python-dotenv
```

## Installation

- Clone the repository:

```bash
git clone https://github.com/yourusername/jumia-ug-scraper.git
cd jumia-ug-scraper
```

## Install the required dependencies

```bash
pip install -r requirements.txt
```

## Setting up the API Key

This script uses ScraperAPI to manage requests and bypass anti-scraping measures. Follow these steps to set up your API key:

- Obtain an API Key
  Sign up at ScraperAPI and get your API key.

- Create a .env File
  In the root directory of the project, create a file named .env.

- Add Your API Key
  Add your ScraperAPI key to the .env file as follows:

```bash
SCRAPERAPI_KEY=your_api_key_here
```

## Security Note

Make sure to add .env to your .gitignore file to prevent the API key from being exposed:

```txt
.env
```

Alternatively, you can set the API key as an environment variable:

## Usage

Ensure your .env file is correctly set up with your ScraperAPI key.

## Output

The output CSV file (scraped_products.csv) will contain the following columns:

Name: Product name
Price: Product price
Link: URL to the product page on Jumia

## How It Works

Scraping

The script starts at page 1 of the Phones & Tablets category.
It constructs the URL for each page using the base URL and page number.
Uses ScraperAPI to send requests, ensuring anti-scraping measures are bypassed.
BeautifulSoup is used to parse the HTML and extract product names, prices, and links.
If no products are found on a page, the scraper stops.
Saving Data

The extracted product information is saved to a CSV file (scraped_products.csv) using the csv module.
The file includes headers: Name, Price, and Link.
Error Handling

If a request fails or an exception occurs, an error message is displayed, and the scraper stops.

## Contributing

Contributions are welcome! If you find any bugs or have feature requests, please open an issue or submit a pull request.

## Environment Variables (.env)

Example of a complete `.env` file structure:

```bash
# ScraperAPI Key (required)
SCRAPERAPI_KEY=your_api_key_here
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.
