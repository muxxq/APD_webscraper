from bs4 import BeautifulSoup

def parse_emag(html):
    if not html:
        return []
        
    soup = BeautifulSoup(html, 'html.parser')
    
    # Try multiple common selectors for product cards
    products = soup.find_all("div", class_=["card-v2", "card-item", "product-item"])
    
    if not products:
        # Check if it's a CAPTCHA or blocking page
        if "captcha" in html.lower() or "robot" in html.lower() or "automat" in html.lower():
            print("Warning: Detected potential blocking/CAPTCHA page.")
        return []
    
    parsed_data = []
    for product in products:
        # Try different selectors for title and price
        title_element = product.find(["a", "h2"], class_=["card-v2-title", "product-title", "card-item-title"])
        price_element = product.find(["p", "span"], class_=["product-new-price", "card-item-new-price"])
        
        if title_element and price_element:
            title = title_element.text.strip()
            # Clean price string: remove currency, whitespace and non-numeric chars except dot/comma
            price_text = price_element.text.strip()
            # Handle eMAG specific price format (e.g. 1.234,56 Lei)
            price = price_text.split('Lei')[0].strip()
            parsed_data.append({"Store": "eMAG", "Product": title, "Price": price})
            
    return parsed_data
