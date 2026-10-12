fh = open("text.txt", "w")
fh.write("Hello world!")
fh.close()

fh = open("text.txt", "r")

while True:
    symbol = fh.read(1)
    if len(symbol) == 0:
        break
    print(symbol)

fh.close()