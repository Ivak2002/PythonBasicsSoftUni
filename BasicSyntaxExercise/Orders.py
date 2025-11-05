number_of_orders = int(input())
total_sum_of_coffee_for_each_day = 0
total_sum_of_coffee = 0

for orders in range(number_of_orders):
    price_per_capsule = float(input())
    serve_days = int(input())
    capsules_needed_per_day = int(input())

    if price_per_capsule < 0.01 or price_per_capsule > 100.00:
        continue
    elif serve_days < 1 or serve_days > 31:
        continue
    elif capsules_needed_per_day < 1 or capsules_needed_per_day > 2000:
        continue

    total_sum_of_coffee_for_each_day = price_per_capsule*serve_days*capsules_needed_per_day
    print(f"The price for the coffee is: ${'%.2f' % total_sum_of_coffee_for_each_day}")
    total_sum_of_coffee += total_sum_of_coffee_for_each_day

print(f"Total: ${'%.2f' % total_sum_of_coffee}")