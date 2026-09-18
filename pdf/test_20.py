import re

email = "username@domain.com"
pattern = r"(\w+)@(\w+\.\w+)"
match = re.search(pattern, email)

if match:
    print("match: ", match)
    print("match.group(): ", match.group())

    user_name = match.group(1)
    domain_name = match.group(2)
    print("Ім'я користувача: ", user_name)
    print("Домен: ", domain_name)
