from ast import main

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def fetch_page(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def parse_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    books = soup.find_all("article", class_="product_pod")
    return books

def write_to_csv(books,start_time):
    with open('data/output/books.csv', 'w', encoding='utf-8') as csvfile:
        csvfile.write("Title,Price,Execution Time\n")
        for book in books:
            title = book.h3.a['title']
            price = book.find("p", class_="price_color").text.strip()
            csvfile.write(f"{title},{price}\n")
        end_time = time.time() - start_time
        csvfile.write(f"Execution Time: {end_time:.2f} seconds\n")
def main():

    url = "https://books.toscrape.com/catalogue/page-1.html"

    start_time = time.time()

    html = fetch_page(url)
    books = parse_page(html)

    write_to_csv(books,start_time)

if __name__ == "__main__":
    main()