n = int(input())
p = int(input())

mask = ~(1 << p)     # invert mask so only bit p becomes 0
new_number = n & mask
print(new_number)
