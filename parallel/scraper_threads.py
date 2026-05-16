import sys
import os
import time
import concurrent.futures

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from utils import scrape_emag_page, save_and_report, get_scrape_config

def main():
    categories, num_pages = get_scrape_config()
    MAX_WORKERS = 8
    
    print(f"\nStarting parallel scraper (ThreadPool) for eMAG (up to {num_pages} pages)...")
    
    for category in categories:
        start_time = time.time()
        all_data = []
        emag_pages = list(range(1, num_pages + 1))

        print(f"\n[eMAG - {category}] Starting ThreadPool extraction...")
        with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            emag_futures = [executor.submit(scrape_emag_page, p, category, True) for p in emag_pages]
            
            for future in concurrent.futures.as_completed(emag_futures):
                try:
                    products = future.result()
                    if products:
                        all_data.extend(products)
                except Exception as e:
                    print(f"Exception occurred during scraping: {e}")

        save_and_report(all_data, category, 'threads', start_time, project_root)

if __name__ == "__main__":
    main()
