import csv
import os

def write_to_csv(data_list, filepath='data/output/scraped_data.csv', execution_time=None):
    if not data_list:
        print("No data to write.")
        return

    # Ensure the directory exists
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    # Extract headers dynamically from the keys of the first dictionary
    headers = list(data_list[0].keys())
    
    with open(filepath, 'w', encoding='utf-8-sig', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data_list)
        
        # Append execution time if provided
        if execution_time is not None:
            csvfile.write(f"\nExecution Time: {execution_time:.2f} seconds\n")
            print(f"Data saved to {filepath}. Execution Time: {execution_time:.2f} s")
        else:
            print(f"Data saved to {filepath}.")
