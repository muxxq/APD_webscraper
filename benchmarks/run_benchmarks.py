import sys
import os
import time
import concurrent.futures
import matplotlib.pyplot as plt

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from utils import scrape_emag_page

def run_sequential(pages, category):
    start = time.time()
    for page in pages:
        scrape_emag_page(page, category, use_delay=False)
        time.sleep(1)  # Matching seq_scraper delay
    return time.time() - start

def run_threads(pages, category):
    start = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        emag_futures = [executor.submit(scrape_emag_page, p, category, True) for p in pages]
        for future in concurrent.futures.as_completed(emag_futures):
            future.result()
    return time.time() - start

def run_multiprocess(pages, category):
    start = time.time()
    max_workers = min(4, os.cpu_count() or 4)
    with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as executor:
        emag_futures = [executor.submit(scrape_emag_page, p, category, True) for p in pages]
        for future in concurrent.futures.as_completed(emag_futures):
            future.result()
    return time.time() - start

def main():
    sizes = {'small': 3, 'medium': 10, 'large': 30} # limited to 30 to avoid bans
    category = "laptopuri"
    
    results = {
        'Sequential': [],
        'Threads': [],
        'Multiprocess': []
    }
    
    print(f"Starting benchmarks for category '{category}'...\n")
    
    for size_name, num_pages in sizes.items():
        pages = list(range(1, num_pages + 1))
        print(f"--- Benchmarking {size_name.upper()} ({num_pages} pages) ---")
        
        print("Running Sequential...")
        t_seq = run_sequential(pages, category)
        results['Sequential'].append(t_seq)
        
        print("Running Threads...")
        t_thr = run_threads(pages, category)
        results['Threads'].append(t_thr)
        
        print("Running Multiprocess...")
        t_mp = run_multiprocess(pages, category)
        results['Multiprocess'].append(t_mp)
        
        print(f"Results for {num_pages} pages: Seq={t_seq:.2f}s, Thr={t_thr:.2f}s, MP={t_mp:.2f}s\n")

    # Plot Execution Time
    x = list(sizes.values())
    
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(x, results['Sequential'], marker='o', label='Sequential')
    plt.plot(x, results['Threads'], marker='s', label='Threads')
    plt.plot(x, results['Multiprocess'], marker='^', label='Multiprocess')
    plt.title('Timp de executie in functie de Numarul de Pagini')
    plt.xlabel('Numar de Pagini')
    plt.ylabel('Timp (secunde)')
    plt.legend()
    plt.grid(True)
    
    # Plot Speedup
    plt.subplot(1, 2, 2)
    speedup_thr = [results['Sequential'][i] / results['Threads'][i] for i in range(len(x))]
    speedup_mp = [results['Sequential'][i] / results['Multiprocess'][i] for i in range(len(x))]
    
    plt.plot(x, speedup_thr, marker='s', label='Speedup Threads')
    plt.plot(x, speedup_mp, marker='^', label='Speedup Multiprocess')
    plt.plot(x, [1]*len(x), 'k--', label='Baseline (Sequential)')
    plt.title('Speedup relativ la executia Secventiala')
    plt.xlabel('Numar de Pagini')
    plt.ylabel('Factor de Speedup')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    output_dir = os.path.join(project_root, 'data', 'output')
    os.makedirs(output_dir, exist_ok=True)
    plot_path = os.path.join(output_dir, 'benchmark_results.png')
    plt.savefig(plot_path)
    print(f"Graficele au fost salvate in {plot_path}")
    
    # Also save the raw data
    data_path = os.path.join(output_dir, 'benchmark_data.csv')
    with open(data_path, 'w', encoding='utf-8') as f:
        f.write("Pages,Sequential_Time,Threads_Time,Multiprocess_Time,Threads_Speedup,Multiprocess_Speedup\n")
        for i in range(len(x)):
            f.write(f"{x[i]},{results['Sequential'][i]:.2f},{results['Threads'][i]:.2f},{results['Multiprocess'][i]:.2f},{speedup_thr[i]:.2f},{speedup_mp[i]:.2f}\n")
    print(f"Datele brute au fost salvate in {data_path}")
    
    plt.show()

if __name__ == '__main__':
    main()
