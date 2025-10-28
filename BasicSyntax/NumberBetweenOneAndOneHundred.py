while True:
    next_number = float(input())
    current_number = next_number

    if 1 <= current_number <= 100:
        print(f"The number {current_number} is between 1 and 100")
        break