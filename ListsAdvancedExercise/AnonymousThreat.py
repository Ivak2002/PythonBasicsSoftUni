def merge(data, start, end):
    start = max(start, 0)
    end = min(end, len(data) - 1)

    merged = "".join(data[start:end+1])
    return data[:start] + [merged] + data[end+1:]


def divide(data, index, parts):
    word = data[index]
    part_len = len(word) // parts
    new_parts = []

    for i in range(parts - 1):
        new_parts.append(word[i*part_len:(i+1)*part_len])

    new_parts.append(word[(parts-1)*part_len:])
    return data[:index] + new_parts + data[index+1:]


data = input().split()

command = input()
while command != "3:1":
    parts = command.split()
    action = parts[0]

    if action == "merge":
        start = int(parts[1])
        end = int(parts[2])
        data = merge(data, start, end)

    elif action == "divide":
        index = int(parts[1])
        partitions = int(parts[2])
        data = divide(data, index, partitions)

    command = input()

print(" ".join(data))
