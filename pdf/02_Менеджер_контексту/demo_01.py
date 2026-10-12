fh = open('text.txt', 'w')
try:
    # Виконання операцій з файлом
    fh.write('Some data')
finally:
    # Закриття файлу в блоці finally гарантує, що файл закриється навіть у разі помилки
    fh.close()
