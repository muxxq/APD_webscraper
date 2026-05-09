from bs4 import BeautifulSoup

def parse_emag(html):
    if not html:
        return []
        
    soup = BeautifulSoup(html, 'html.parser')
    
    products = soup.find_all("div", class_="card-v2")
    
    parsed_data = []
    for product in products:
        title_element = product.find("a", class_="card-v2-title")
        price_element = product.find("p", class_="product-new-price")
        
        if title_element and price_element:
            title = title_element.text.strip()
            price = price_element.text.replace('Lei', '').replace('&#46;', '.').strip()
            parsed_data.append({"Store": "eMAG", "Product": title, "Price": price})
            
    return parsed_data
