n = int(input())
p = int(input())

mask = 7 << p     # 7 = 111
result = n ^ mask

print(result)
