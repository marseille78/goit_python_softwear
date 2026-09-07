string = 'break statement'

for letter in string:
    print(letter)
    if letter == 'e' or letter == 's':
        break

print('Out of thr loop')