import requests
from bs4 import BeautifulSoup
from collections import defaultdict

url = "https://cuantoestaeldolar.pe/"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
first_div = soup.find('div', {'class': 'mx-1 md:mx-3'})
hidden_divs = first_div.find_all('div', {'class': 'hidden md:block'})

result = {}
for i, hidden_div in enumerate(hidden_divs):
    exchange_div = hidden_div.find('div', {'class': 'exchange_div flex justify-center'})
    if exchange_div:
        values = []
        p_elements = exchange_div.find_all('p', {'class': 'ValueQuotation_text___mR_0'})
        for p in p_elements:
            values.append(p.text)
        result[f"{i}"] = values

for group, values in result.items():
    print(f"{group}: {values}")