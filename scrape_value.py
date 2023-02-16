"""
Author: totallynotdavid
Date: 16/02/2023
"""

import requests
from bs4 import BeautifulSoup

URL = "https://cuantoestaeldolar.pe/"
response = requests.get(URL, timeout=5)

soup = BeautifulSoup(response.text, 'html.parser')
first_div = soup.find('div', {'class': 'mx-1 md:mx-3'})

hidden_divs = first_div.find_all('div', {'class': 'hidden md:block'}) # type: ignore
result = {}

for i, hidden_div in enumerate(hidden_divs):
    exchange_div = hidden_div.find('div', {'class': 'exchange_div flex justify-center'})
    values = []
    p_elements = exchange_div.find_all('p', {'class': 'ValueQuotation_text___mR_0'})
    for p in p_elements:
        values.append(p.text)
    result[f"{i}"] = values

for group, values in result.items():
    print(f"{group}: ")
    for i, value in enumerate(values):
        LABEL = "Compra" if i == 0 else "Venta"
        print(f"{LABEL}: {value}")
