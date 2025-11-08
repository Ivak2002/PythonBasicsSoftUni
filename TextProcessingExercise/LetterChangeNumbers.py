parts = input().split()
total = 0

for p in parts:
    first = p[0]
    last = p[-1]
    number = int(p[1:-1])

    if first.isupper():
        number /= (ord(first) - 64)
    else:
        number *= (ord(first) - 96)

    if last.isupper():
        number -= (ord(last) - 64)
    else:
        number += (ord(last) - 96)

    total += number

print(f"{total:.2f}")
