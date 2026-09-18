map = {
    ord('т'): 't',
    ord('ю'): 'yu',
    ord('Т'): 'T',
    ord('Ю'): 'YU',
}

# print('T', ord('T'))

translated = "філватжліваюіттіваіявюів".translate(map)
print(translated)