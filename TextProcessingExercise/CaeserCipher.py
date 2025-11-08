text = input()
encrypted = "".join(chr(ord(ch) + 3) for ch in text)
print(encrypted)
