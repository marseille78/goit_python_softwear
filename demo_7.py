string_input = input("Enter string: ")
string_to_compare = input("Enter string to compare: ")

for char in set(string_input):
    print(char)
    if char not in string_to_compare:
        print(False)
        break
else:
    print(True)