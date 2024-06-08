# Full Top XRP AMM Scraper

This project contains a Python script to scrape data from multiple pages on the XRPScan Automated Market Makers (AMM) pools page. The script uses Selenium to navigate through the pages and BeautifulSoup to parse the HTML content and extract the relevant data. The collected data is saved into a JSON file.

## Requirements

Ensure you have the following installed:
- Python 3.x
- Google Chrome browser
- ChromeDriver (compatible with your Chrome browser version)
- Required Python packages:
  - `selenium`
  - `beautifulsoup4`
  - `pandas`

## Setup

1. **Install Google Chrome**: Make sure you have Google Chrome installed on your system.
2. **Download ChromeDriver**: Download the ChromeDriver that matches your version of Chrome from [here](https://sites.google.com/chromium.org/driver/). Make sure to add ChromeDriver to your system PATH.
3. **Install Required Python Packages**:
    ```sh
    pip install selenium beautifulsoup4 pandas
    ```

## Usage

1. **Clone the Repository**:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Run the Script**:
    Execute the script to scrape the data and save it into a JSON file:
    ```sh
    python full_top_xrp_amm_scrape.py
    ```

## Script Explanation

The script performs the following tasks:

1. **Setup Selenium WebDriver**: Initializes the Selenium WebDriver with options to ignore certificate errors.
2. **Fetch the Web Page**: Navigates to the URL.
3. **Wait for Page Load**: Waits for the page to fully load and the table to be present.
4. **Determine Total Pages**: Extracts the total number of pages dynamically from the HTML content.
5. **Scrape Data from Each Page**: Loops through each page, clicking the "Next" button, and scrapes the data.
6. **Save Data**: Saves the scraped data into a JSON file.

### Key Functions

- `scrape_page()`: Scrapes data from the current page and appends it to the lists.
- `main()`: Main function that sets up the WebDriver, handles page navigation, and saves the data.

## JSON Output

The script outputs the data in a JSON file `output\full_top_amm_data_complete.json` with the following structure:

```json
{
    "Rank": [...],
    "Asset Pair": [...],
    "Market": [...],
    "AMM Account": [...],
    "XRP Locked": [...],
    "Trading Fee": [...],
    "LPToken Balance": [...]
}
