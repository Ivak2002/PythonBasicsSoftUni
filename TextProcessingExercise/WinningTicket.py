tickets = [t.strip() for t in input().split(",")]

symbols = "@#$^"

for ticket in tickets:
    if len(ticket) != 20:
        print("invalid ticket")
        continue

    left = ticket[:10]
    right = ticket[10:]

    best_match = ""

    for sym in symbols:
        left_count = max((len(s) for s in left.split(sym) if s == ""), default=0)
        right_count = max((len(s) for s in right.split(sym) if s == ""), default=0)

        match_length = min(left_count, right_count)

        if match_length >= 6:
            best_match = (sym, match_length)
            break

    if not best_match:
        print(f'ticket "{ticket}" - no match')
    else:
        sym, count = best_match
        if count == 10:
            print(f'ticket "{ticket}" - {count}{sym} Jackpot!')
        else:
            print(f'ticket "{ticket}" - {count}{sym}')
