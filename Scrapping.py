from bs4 import BeautifulSoup
import requests

AMAZON_KEYBOARD_URL = 'https://www.amazon.com.mx/Granvela-MechanicalEagle-Multicolor-Retroiluminada-US-Layout/dp/B01DBVGZSA/ref=sr_1_1?__mk_es_MX=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3LVJ9S4G84V86&keywords=teclado+mecanico&qid=1575003714&sprefix=Teclado%2Caps%2C229&sr=8-1'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

def check_price():
    page = requests.get(AMAZON_KEYBOARD_URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_saleprice").get_text()
    converted_price = float(price[0:5])

    print(converted_price)
    print(title.strip())

check_price()

