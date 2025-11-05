number_of_messages = int(input())

message_text = ""

for current_message in range(number_of_messages):
    message = int(input())

    if message == 88:
        message_text = "Hello"
    elif message == 86:
        message_text = "How are you?"
    elif message < 88:
        message_text = "GREAT!"
    else:
        message_text = "Bye."

    print(message_text)