# Функции

def greeting(**kwargs): # -> kwargs = {'key_1': value_1, ..., 'key_n': value_n}
    print(kwargs)
    name = kwargs.get('name', 'Unknown')
    age = kwargs.get('age', 100)
    print(f"Hello {name}, you are {age} years old.")

greeting(name="Ruslan", lang="ukr", student=True)
greeting(name="Ruslan", lang="ukr", student=True, age=22)