import sys
import os
import time

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from utils import fetch_page, write_to_csv
from utils.parsers.emag_parser import parse_emag
from utils.parsers.altex_parser import parse_altex

def main():
    NUM_PAGES = 5
    
    print(f"Starting sequential scraper for eMAG and Altex (up to {NUM_PAGES} pages)...")
    start_time = time.time()
    
    all_data = []

    # 1. Scrape eMAG
    print("\n[eMAG] Starting extraction...")
    for page in range(1, NUM_PAGES + 1):
        url = f"https://www.emag.ro/laptopuri/p{page}/c"
        print(f"Fetching eMAG Page {page}: {url}")
        
        html = fetch_page(url)
        if html:
            products = parse_emag(html)
            print(f"Extracted {len(products)} products.")
            all_data.extend(products)
            
        time.sleep(1) 

    # 2. Scrape Altex
    print("\n[Altex] Starting extraction...")
    for page in range(1, NUM_PAGES + 1):
        url = f"https://altex.ro/laptopuri/cpl/filtru/p/{page}/"
        print(f"Fetching Altex Page {page}: {url}")
        
        html = fetch_page(url)
        if html:
            products = parse_altex(html)
            print(f"Extracted {len(products)} products.")
            all_data.extend(products)
            
        time.sleep(1)

    print(f"\nExtraction done. Total products: {len(all_data)}")
    
    if all_data:
        # Salvare in fisier CSV
        output_filepath = os.path.join(project_root, 'data', 'output', 'laptops.csv')
        write_to_csv(all_data, filepath=output_filepath)
        
        total_time = time.time() - start_time
        print(f"\nTime spent: {total_time:.3f} seconds")
    else:
        print("Scraping failed or blocked: No data extracted.")
        total_time = time.time() - start_time
        print(f"\nTime spent: {total_time:.3f} seconds")

if __name__ == "__main__":
    main()