start_index_ascii = int(input())
end_index_ascii = int(input())
character_number = ""
for number in range(start_index_ascii,end_index_ascii + 1):
    character_number = chr(number)
    print(character_number, end=" ")
