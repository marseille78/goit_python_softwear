fh = open("text.txt", "w+")
fh.write("hello!")
fh.seek(0)

first_two_symbols = fh.read(2)
print(first_two_symbols)

fh.close()