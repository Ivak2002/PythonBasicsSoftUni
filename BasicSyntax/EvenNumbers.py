word_count = int(input())
for i in range(word_count):
    number = int(input())
    if not number % 2 == 0:
        print(f"{number} is odd!")
        quit()
print(f"All numbers are even!")