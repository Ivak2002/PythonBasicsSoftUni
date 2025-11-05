group_size = int(input())
days = int(input())

coins = 0
companions = group_size

for day in range(1, days + 1):

    # Every 10th day, 2 companions leave (at the start of the day)
    if day % 10 == 0:
        companions -= 2

    # Every 15th day, 5 companions join (also at the start)
    if day % 15 == 0:
        companions += 5

    # Daily income and food expense
    coins += 50
    coins -= 2 * companions

    # Every 3rd day: motivational party
    if day % 3 == 0:
        coins -= 3 * companions

    # Every 5th day: boss monster
    if day % 5 == 0:
        coins += 20 * companions

        # If it's ALSO a 3rd day → extra spending
        if day % 3 == 0:
            coins -= 2 * companions

# Final coins per companion (rounded down)
coins_each = coins // companions

print(f"{companions} companions received {coins_each} coins each.")
