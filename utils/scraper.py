import os
import time
import random
from utils.fetcher import fetch_page
from utils.parsers.emag_parser import parse_emag
from utils.writer import write_to_csv

def scrape_emag_page(page, category, use_delay=False):
    """Fetches and parses a single eMAG page with retries if 0 products are found."""
    max_retries = 2
    for attempt in range(max_retries + 1):
        if use_delay:
            # respect rate limit and stagger requests
            time.sleep(random.uniform(0.5, 2.0))
            
        url = f"https://www.emag.ro/{category}/p{page}/c"
        if attempt > 0:
            print(f"Retrying eMAG Page {page} (Attempt {attempt})...")
        else:
            print(f"Fetching eMAG Page {page}: {url}")
        
        html = fetch_page(url)
        if html:
            products = parse_emag(html)
            if products:
                print(f"Extracted {len(products)} products from eMAG page {page}.")
                return products
            else:
                if attempt < max_retries:
                    print(f"Warning: Page {page} returned 0 products. Retrying after delay...")
                    time.sleep(random.uniform(2, 5)) # Longer delay for retry
                else:
                    print(f"Failed to extract products from eMAG page {page} after {max_retries} retries.")
        else:
            if attempt < max_retries:
                time.sleep(1)
            
    return []

def save_and_report(all_data, category, method, start_time, project_root):
    """Saves the extracted data to CSV and prints the time spent."""
    print(f"\nExtraction done. Total products: {len(all_data)}")
    
    if all_data:
        output_dir = os.path.join(project_root, 'data', 'output', method)
        os.makedirs(output_dir, exist_ok=True)
        output_filepath = os.path.join(output_dir, f'{category}.csv')
        
        write_to_csv(all_data, filepath=output_filepath)
        
        total_time = time.time() - start_time
        print(f"\nTime spent: {total_time:.3f} seconds")
    else:
        print("Scraping failed or blocked: No data extracted.")
        total_time = time.time() - start_time
        print(f"\nTime spent: {total_time:.3f} seconds")

def get_scrape_config():
    """Prompts the user to input categories and selection size (small, medium, large)."""
    print("=" * 40)
    print("eMAG Scraper - Configurare")
    print("=" * 40)
    print("Format categorie: litere mici, fara spatii, separate prin cratima")
    print("Exemple valide: 'telefoane-mobile', 'laptopuri', 'televizoare'\n")
    
    while True:
        try:
            num_cats_input = input("Introduceți numărul de categorii (ex: 2): ")
            num_cats = int(num_cats_input)
            if num_cats > 0:
                break
            print("Vă rugăm să introduceți un număr mai mare ca 0.\n")
        except ValueError:
            print("Intrare invalidă. Vă rugăm introduceți un număr întreg valid.\n")
            
    categories = []
    print("\n" + "-" * 20)
    for i in range(num_cats):
        cat = input(f"Numele categoriei {i+1}: ").strip().lower()
        cat = cat.replace(" ", "-")
        categories.append(cat)
    print("-" * 20 + "\n")

    print("Selectați dimensiunea extracției:")
    print("1. Small (3 pagini)")
    print("2. Medium (10 pagini)")
    print("3. Large (toate paginile)")
    
    while True:
        choice = input("\nOpțiunea aleasă (1/2/3): ").strip()
        if choice == '1':
            return categories, 3
        elif choice == '2':
            return categories, 10
        elif choice == '3':
            return categories, 100 # We will use 100 as a safe 'large' limit for now
        print("Opțiune invalidă. Alegeți 1, 2 sau 3.")

def get_categories_from_input():
    # Keep this for backward compatibility if needed, but point to the new logic
    cats, _ = get_scrape_config()
    return cats
