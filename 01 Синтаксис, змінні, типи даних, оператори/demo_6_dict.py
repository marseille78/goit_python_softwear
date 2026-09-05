person = {'name': 'Ruslan', 'age': 48, 'phone': '38(098)********', 'student': True}

print(person.get('name', 'Nonane')) # 'Ruslan'
print(person.get('phone', None)) # '38(098)********'
print(person.get('lang', None)) # None

print(person["name"]) # 'Ruslan'
print(person["lang"]) # KeyError