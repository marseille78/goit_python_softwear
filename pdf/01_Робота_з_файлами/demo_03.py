fh = open("text.txt", "w")
fh.write("Hello World!")
fh.close()

fh = open("text.txt", "r")
all_file = fh.read()
print(all_file)
fh.close()