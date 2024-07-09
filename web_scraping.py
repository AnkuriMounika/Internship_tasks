import requests
from bs4 import BeautifulSoup
import csv

def scrape_amazon_product_data():
    url = "https://www.amazon.com/s?k=product"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    products = []
    for item in soup.select('.s-main-slot .s-result-item'):
        name = item.select_one('h2 a span').text.strip() if item.select_one('h2 a span') else 'N/A'
        price = item.select_one('.a-price-whole').text.strip() if item.select_one('.a-price-whole') else 'N/A'
        rating = item.select_one('.a-icon-alt').text.strip() if item.select_one('.a-icon-alt') else 'N/A'
        products.append([name, price, rating])

    return products

def save_to_csv(data, filename='products.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Price", "Rating"])
        writer.writerows(data)

if __name__ == "__main__":
    product_data = scrape_amazon_product_data()
    save_to_csv(product_data)
    print("Data has been saved to products.csv")
