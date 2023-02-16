"""
Author: totallynotdavid
Date: 16/02/2023
"""

import json

with open('results.json', 'r', encoding='utf-8') as f:
    results = json.load(f)

sorted_results = sorted(results, key=lambda x: float(x['Compra']))[:3]

for i, result in enumerate(sorted_results):
    print(f"#{i+1}: Minimum Compra value: {result['Compra']}")
    print(f"     Image source: {result['ImageSrc']}")

# Write the results to a file
with open('minimum_price.json', 'w', encoding='utf-8') as f:
    json.dump(sorted_results, f, indent=4)

print("Results written to file 'minimum_price.json'")
