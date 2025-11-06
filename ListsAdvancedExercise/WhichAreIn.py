def finding_sub_string(first_string,second_string):
    """
    This function compares two strings and finds matching substrings.
    """
    new_list = []
    for word in first_string:
        for word_two in second_string:
            if word in word_two:
                new_list.append(word)
                break
    return new_list


string_first = input().split(", ")
string_second = input().split(", ")
string_new = finding_sub_string(string_first,string_second)
print(string_new)
