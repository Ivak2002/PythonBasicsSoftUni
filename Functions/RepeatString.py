def string_repeat_print(string,repetitions):
    new_string = ''
    for repetition in range(repetitions):
        new_string += string
    print(new_string)


text = input()
repetition_times = int(input())
string_repeat_print(text,repetition_times)
