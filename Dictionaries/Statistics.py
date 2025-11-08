dict_products = {}
while True:
    string_products = input().split(": ")
    if string_products.__contains__("statistics"):
        break

    product = string_products[0]
    quantity = int(string_products[1])

    if product not in dict_products:
        dict_products[product] = 0
    dict_products[product] += quantity

print(f"Products in stock:")
for product,quantity in dict_products.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(dict_products.keys())}")
print(f"Total Quantity: {sum(dict_products.values())}")


