numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
header = '|{:^15}|{:^15}|{:^15}|'.format('int', 'int^2', 'int^3')
separator = '-' * len(header)
body = ''

for num in numbers:
    body += '|{:^15}|{:^15}|{:^15}|\n'.format(num, num ** 2, num ** 3)

table = '\n'.join([separator, header, separator, body, separator])

print(table)