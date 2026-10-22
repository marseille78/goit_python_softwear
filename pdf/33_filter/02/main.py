some_str = 'Видавництво А-БА-БА-ГА-ЛА-МА-ГА'

new_str = ''.join(list(filter(lambda x: x.islower(), some_str)))

print(new_str)