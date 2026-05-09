from bs4 import BeautifulSoup

def parse_altex(html):
    if not html:
        return []
        
    soup = BeautifulSoup(html, 'html.parser')
    
    products = soup.find_all("li", class_="Products-item")
    
    parsed_data = []
    for product in products:
        title_element = product.find("span", class_="Product-name")
        price_element = product.find("span", class_="Price-int")
        price_decimals = product.find("sup")
        
        if title_element and price_element:
            title = title_element.text.replace('\n', '').strip()
            
            price_int = price_element.text.strip()
            price_dec = price_decimals.text.strip() if price_decimals else ""
            
            # Formateaza pretul clar 
            price = price_int.replace('.', '') + price_dec.replace(',', '.')
            parsed_data.append({"Store": "Altex", "Product": title, "Price": price})
            
    return parsed_data
