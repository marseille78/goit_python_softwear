# Записати у довідник кількість кожного елемента, який передається у строці

def char_counter(sentence):
    operator_dict = dict()

    for char in sentence:
        if char not in operator_dict.keys():
            operator_dict[char] = 1
        else:
            operator_dict[char] += 1

    return operator_dict

user_input = input("Enter a sentence: ")

print(char_counter(user_input))
print(char_counter(user_input).keys())
print(char_counter(user_input).values())