points = 0

while True:
    activity = input()

    if activity == "END":
        break

    if activity == "cat" or activity == "dog" or activity == "coding" or activity == "movie":
        points += 1
    if activity == "CAT" or activity == "DOG" or activity == "CODING" or activity == "MOVIE":
        points += 2


if points > 5:
    print("You need extra sleep")
else:
    print(points)

