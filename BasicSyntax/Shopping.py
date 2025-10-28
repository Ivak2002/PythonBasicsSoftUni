budget = int(input())
total_sum = 0


while True:
    product = input()

    if product == 'End':
        print('You bought everything needed.')
        break

    product_int = int(product)

    if total_sum + product_int > budget:
        print("You went in overdraft!")
        break

    total_sum += product_int