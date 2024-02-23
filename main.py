from typing import List, Any

import requests
from bs4 import BeautifulSoup

url = 'https://dirtycoins.vn/shop'

response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, 'html.parser')

title = soup.find('title').text
list_img_tag = soup.find_all('img', class_='lazyload')
list_content = soup.find_all('div',class_='product-content')
list_price:list[Any] = []
list_content_text: list[Any]=[]

for img_tag in list_img_tag:
    src = img_tag.get('src')
    if src:
        print(src)

for item_content in list_content:
    list_content_h3 = item_content.find('h3')
    list_content_text.append(item_content.find('a').text)

    div_price = item_content.find('div',class_='product-price')



print(list_content_text)