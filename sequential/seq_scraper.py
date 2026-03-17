import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

url = "https://books.toscrape.com/catalogue/page-1.html"

response = requests.get(url)
print('status', response.status_code)
soup = BeautifulSoup(response.text, 'html.parser')

books = soup.find_all("article", class_="product_pod")
print('found books', len(books))

for book in books:
    title = book.h3.a['title']
    price = book.find("p", class_="price_color").text.strip()
    print(f"Title: {title}, Price: {price}")