n = int(input())
b = input()   # "0" or "1"

binary = bin(n)[2:]     # remove '0b'
count = binary.count(b)

print(count)
