def order_calculator_and_print_price(order,quantity):
    price = 0
    if order == "coffee":
        price = 1.50 * quantity
    elif order == "water":
        price = 1.00 * quantity
    elif order == "coke":
        price = 1.40 * quantity
    else:
        price = 2.00 * quantity

    print(f"{'%.2f' % price}")


purchase = input()
purchase_quantity = int(input())
order_calculator_and_print_price(purchase,purchase_quantity)