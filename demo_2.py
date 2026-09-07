entry_password = input("Enter password: ")

print(id(entry_password), id('test2024'), sep='\n')

if entry_password == 'test2024':
    print("Access Granted")
else:
    print("Access Denied")