string_products = input().split()
searched_for_products = input().split()
dict_products = {}
for product in range(0,len(string_products), 2):
    food = string_products[product]
    quantity = string_products[product + 1]
    dict_products[food] = int(quantity)

for available_product in searched_for_products:
    if available_product in dict_products:
        print(f"We have {dict_products[available_product]} of {available_product} left")
    else:
        print(f"Sorry, we don't have {available_product}")


