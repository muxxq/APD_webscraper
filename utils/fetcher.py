def fetch_page(url, timeout=15):
    try:
        try:
            from curl_cffi import requests as cffi_requests
            # 'impersonate="chrome"' is the bypass
            response = cffi_requests.get(url, impersonate="chrome", timeout=timeout)
        except ImportError:
            import requests
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0 Safari/537.36'
            }
            response = requests.get(url, headers=headers, timeout=timeout)
            
        return response.text
    except Exception as e:
        print(f"Error fetching URL {url}: {e}")
        return None
