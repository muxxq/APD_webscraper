import time

def fetch_page(url, timeout=25, retries=3):
    for attempt in range(retries):
        try:
            try:
                from curl_cffi import requests as cffi_requests
                # 'impersonate="chrome110"' bypasses Cloudflare checks
                response = cffi_requests.get(url, impersonate="chrome110", timeout=timeout)
            except ImportError:
                import requests
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                    'Accept-Language': 'en-US,en;q=0.9,ro;q=0.8',
                }
                response = requests.get(url, headers=headers, timeout=timeout)
                
            if response.status_code == 200:
                return response.text
            else:
                print(f"Warning: Page {url} returned status code {response.status_code}")
                return None
        except Exception as e:
            print(f"Error fetching URL {url} (Attempt {attempt + 1}/{retries}): {e}")
            if attempt < retries - 1:
                time.sleep(2) # Backoff before retry
            else:
                return None
    return None
