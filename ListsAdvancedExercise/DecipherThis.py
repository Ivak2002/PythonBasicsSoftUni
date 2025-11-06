def decipher_word(word):
    # extract leading number
    digits = ""
    for ch in word:
        if ch.isdigit():
            digits += ch
        else:
            break

    first_letter = chr(int(digits))
    rest = word[len(digits):]

    if len(rest) > 1:
        rest = rest[-1] + rest[1:-1] + rest[0]

    return first_letter + rest


def decipher_text(text):
    words = text.split()
    return " ".join(decipher_word(w) for w in words)


message = input()
print(decipher_text(message))
