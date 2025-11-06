def loading_bar(num):
    percent_count = num // 10           # how many '%' symbols
    dots_count = 10 - percent_count     # how many '.' symbols

    bar = "[" + "%" * percent_count + "." * dots_count + "]"

    if num == 100:
        return f"100% Complete!\n{bar}"
    else:
        return f"{num}% {bar}\nStill loading..."


number = int(input())
print(loading_bar(number))
