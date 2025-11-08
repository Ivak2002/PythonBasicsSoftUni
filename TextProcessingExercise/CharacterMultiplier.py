s1, s2 = input().split()

total = 0
length = max(len(s1), len(s2))

for i in range(length):
    if i < len(s1) and i < len(s2):
        total += ord(s1[i]) * ord(s2[i])
    elif i < len(s1):
        total += ord(s1[i])
    else:
        total += ord(s2[i])

print(total)
