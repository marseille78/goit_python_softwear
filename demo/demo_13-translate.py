trans_map = {
    ord('Я'): 'Ya',
    ord('н'): 'n',
    ord('а'): 'a',
}

ukr_name = 'Яна'

lat_name = ukr_name.translate(trans_map)

print(ukr_name, '=', lat_name, sep=' ')