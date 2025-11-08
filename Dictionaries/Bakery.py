string_products = input().split()
dict_products = {}
for product in range(0,len(string_products), 2):
    food = string_products[product]
    quantity = string_products[product + 1]
    dict_products[food] = int(quantity)
print(dict_products)
