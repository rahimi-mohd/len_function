def string_length(string):
    index = 0

    while True:
        try:
            string[index] #this will loop all alphabet in string
            index += 1
        except:
            break

    return index


user_input = input("Insert string: ")
print(string_length(user_input))
print(len(user_input)) # debug
