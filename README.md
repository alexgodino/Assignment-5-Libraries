DATA 4000 – Assignment 5: Libraries

This repository contains my solutions for Assignment 5 in DATA 4000. The goal was to combine conditionals, loops, exception handling, functions, and basic API usage in Python.


Files:  
pos_checkout.py – point-of-sale checkout system with input validation and discounts  
inventory_spotcheck.py – inventory analyzer with reorder logic and API spot check


How to Run:

Run each file from the terminal  
```bash
pip install requests
python pos_checkout.py
```

Install required library:  
```bash
pip install requests
```

Example Run – pos_checkout.py  
```bash
Student key: abc123
Item name: apple
Unit price: 2.5
Quantity: 3
Item name: DONE

Seed: 444
Units: 3
Subtotal: $7.50
Discount: 0%
Perk applied: NO
Total: $7.50
```
Example Run – inventory_spotcheck.py
```bash
Student key: abc123
SKU: A101
On hand: 5
SKU: B202
On hand: 20
SKU: DONE

Seed: 444
Threshold: 15
SKUs entered: 2
Reorder flagged: 1
Spotcheck term: weezer
Songs returned: 5
API status: OK
```
