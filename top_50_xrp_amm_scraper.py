import pandas as pd
from bs4 import BeautifulSoup
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import json
import time

# Set up the Selenium WebDriver with options to ignore certificate errors
options = webdriver.ChromeOptions()
options.set_capability("acceptInsecureCerts", True)

driver = webdriver.Chrome(options=options)

# Fetch the web page
url = ""
driver.get(url)

# Wait for the page to fully load and for the table to be present
try:
    # Wait for the document ready state to be complete
    WebDriverWait(driver, 20).until(
        lambda d: d.execute_script('return document.readyState') == 'complete'
    )
    # Wait for the table to be present
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.TAG_NAME, 'table'))
    )
except Exception as e:
    print("Error: ", e)
    driver.quit()

# Allow some additional time for dynamic content to load
time.sleep(5)

# Get the page source
html_content = driver.page_source

# Save the HTML content to a file
with open("zscraped_amm_pool.htm", "w", encoding="utf-8") as file:
    file.write(html_content)

# Load the HTML file
with open('zscraped_amm_pool.htm', 'r', encoding='utf-8') as file:
    content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')

# Find all tables in the HTML file
tables = soup.find_all('table')

# Extract the relevant table by inspecting its content
# Based on the provided example, the relevant data appears to be in the second table (index 1)
relevant_table = tables[1]

# Initialize lists to store the data
ranks = []
asset_pairs = []
markets = []
amm_accounts = []
xrp_locked = []
trading_fees = []
lptoken_balances = []

# Iterate over the rows in the table and extract the data with corrected column indices
rows = relevant_table.find_all('tr')
for row in rows[1:]:  # Skip the header row
    columns = row.find_all('td')
    if len(columns) >= 7:  # Check if the row contains the necessary columns
        rank = columns[0].get_text(strip=True)
        asset_pair = columns[1].get_text(strip=True)
        market = columns[2].get_text(strip=True)
        amm_account = columns[3].get_text(strip=True)
        xrp_locked_value = columns[4].get_text(strip=True)
        trading_fee_value = columns[5].get_text(strip=True)
        lptoken_balance_value = columns[6].get_text(strip=True)
        
        ranks.append(rank)
        asset_pairs.append(asset_pair)
        markets.append(market)
        amm_accounts.append(amm_account)
        xrp_locked.append(xrp_locked_value)
        trading_fees.append(trading_fee_value)
        lptoken_balances.append(lptoken_balance_value)

# Create the dictionary
data_dict = {
    "Rank": ranks,
    "Asset Pair": asset_pairs,
    "Market": markets,
    "AMM Account": amm_accounts,
    "XRP Locked": xrp_locked,
    "Trading Fee": trading_fees,
    "LPToken Balance": lptoken_balances
}

# Convert to JSON
json_data = json.dumps(data_dict, indent=4)

# Save to a JSON file
json_file_path = '50top_amm_data_complete.json'
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json_file.write(json_data)

# Print the resulting JSON data to verify
print(json_data)
