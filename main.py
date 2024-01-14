import requests
from bs4 import BeautifulSoup


def get_coffee_prices():
    url = "https://www.google.com.br/search?q=café+especial&sca_esv=598249058&tbm=shop&sxsrf=ACQVn0_4JnCBaFPRJUkulFG1gMD6qFwigg%3A1705190871611&ei=1yWjZcifJPzZ1sQPxoqS-AM&udm=&ved=0ahUKEwiI57OBy9uDAxX8rJUCHUaFBD8Q4dUDCAg&uact=5&oq=café+especial&gs_lp=Egtwcm9kdWN0cy1jYyIOY2Fmw6kgZXNwZWNpYWwyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAESKQPUNsBWJgNcAB4AJABAJgBpwGgAdAIqgEDMy43uAEDyAEA-AEBwgIIEAAYgAQYsAPCAgcQABiABBgKiAYBkAYK&sclient=products-cc"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')
    products = soup.find_all('div', class_='KZmu8e')
    for _, product in enumerate(products, start=1):
        product_name = product.find('h3', class_='sh-np__product-title translate-content').text.strip()
        product_price = product.find('span', class_='T14wmb').text.strip()
        product_price = product_price.split("R$")
        print(f"Produto: {product_name}")
        print(f"Preço: {product_price[1].replace(r"\xa", "")}")
        print("-" * 50)

if __name__ == "__main__":
    get_coffee_prices()
