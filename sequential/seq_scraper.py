import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

url = "https://books.toscrape.com/catalogue/page-1.html"

start_time = time.time()

response = requests.get(url)
print('status', response.status_code)
soup = BeautifulSoup(response.text, 'html.parser')

books = soup.find_all("article", class_="product_pod")
print('found books', len(books))

for book in books:
    title = book.h3.a['title']
    price = book.find("p", class_="price_color").text.strip()
    print(f"Title: {title}, Price: {price}")

with open('data/output/books.csv', 'w', encoding='utf-8') as f:
    f.write("Title,Price\n")
    for book in books:
        title = book.h3.a['title']
        price = book.find("p", class_="price_color").text.strip()
        f.write(f"{title},{price}\n")

end_time = time.time()
print(f"Execution time: {end_time - start_time:.2f} seconds")