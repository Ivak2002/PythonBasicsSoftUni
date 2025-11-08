info_dict = dict()
data = input()
split_data = list()
while True:
    if ":" not in data:
        if "_" in data:
            data = data.split("_")
            data = " ".join(data)
        for key,value in info_dict.items():
            for inner_key,inner_value in value.items():
                if inner_value == data:
                    print(f"{key} - {inner_key}")
        break
    split_data = data.split(":")
    name = ""
    id_code = 0
    course = ""
    for info in split_data:
        name = split_data[0]
        id_code = int(split_data[1])
        course = split_data[2]
        info_dict[name] = {id_code:course}
    data = input()
