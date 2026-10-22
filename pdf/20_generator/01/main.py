def cound_down(start):
    while start > 0:
        yield start
        start -= 1


for number in cound_down(5):
    print(number)