usernames = input().split(", ")

for name in usernames:
    if 3 <= len(name) <= 16 and all(ch.isalnum() or ch in "-_" for ch in name):
        print(name)
