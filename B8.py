product = {
    "name": "Laptop",
    "brand": "Dell",
    "price": 75000,
    "quantity": 5
}

print(product["name"])
print(product["brand"])
print(product["price"])
print(product["quantity"])

total_value = product["price"] * product["quantity"]

print(total_value)

product["quantity"]=2
print(product)