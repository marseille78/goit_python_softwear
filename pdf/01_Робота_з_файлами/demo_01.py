fh = open('text.txt', 'w')
symbols_written = fh.write("Hello!")
print(symbols_written) # 6
fh.close()