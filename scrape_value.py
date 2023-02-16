"""
Author: totallynotdavid
Date: 16/02/2023
"""

import json
import requests
from bs4 import BeautifulSoup

URL = "https://cuantoestaeldolar.pe/"
response = requests.get(URL, timeout=5)

soup = BeautifulSoup(response.text, 'html.parser')
first_div = soup.find('div', {'class': 'mx-1 md:mx-3'})
hidden_divs = first_div.find_all('div', {'class': 'hidden md:block'}) # type: ignore

result = []
for i, hidden_div in enumerate(hidden_divs):
    exchange_div = hidden_div.find('div', {'class': 'exchange_div flex justify-center'})
    exchange_img = hidden_div.find_all('img')

    if exchange_div and exchange_img:
        values = []

        p_elements = exchange_div.find_all('p', {'class': 'ValueQuotation_text___mR_0'})
        for p in p_elements:
            values.append(p.text)

        for img in exchange_img:
            img_src = img.get('src', '')

        result.append ({
            "Compra": values[0],
            "Venta": values[1],
            "ImageSrc": img_src
        })

# Write the results to a file
with open('results.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, indent=4)

print("Results written to file 'results.json'")
