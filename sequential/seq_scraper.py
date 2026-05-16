import sys
import os
import time

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from utils import scrape_emag_page, save_and_report, get_scrape_config

def main():
    categories, num_pages = get_scrape_config()
    
    print(f"\nStarting sequential scraper for eMAG (up to {num_pages} pages)...")
    
    for category in categories:
        start_time = time.time()
        all_data = []

        print(f"\n[eMAG - {category}] Starting extraction...")
        for page in range(1, num_pages + 1):
            products = scrape_emag_page(page, category, use_delay=False)
            if not products:
                print(f"No more products found on page {page}. Stopping.")
                break
            all_data.extend(products)
            time.sleep(1)

        save_and_report(all_data, category, 'secvential', start_time, project_root)

if __name__ == "__main__":
    main()