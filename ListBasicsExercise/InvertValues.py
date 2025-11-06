string = input().split()
string_as_integers = []
for number in string:
    int_number = -int(number)
    string_as_integers.append(int_number)
print(string_as_integers)