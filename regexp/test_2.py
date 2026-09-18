import re

string = "Niels Bohr was born to Christian Bohr (1858-1911), a professor of physiology at the University of Copenhagen,"\
         "twice a candidate for the Nobel Prize in physiology and medicine,[10] and Ellen Adler (" \
         "1860-1930), daughter of the influential and very wealthy Jewish banker and liberal parliamentarian David " \
         "Baruch Adler (1826—1878) and Jenny Raphael (1830-1902) of the British Jewish " \
         "Raphael Raphael & sons[en][11] of the British Jewish banking dynasty. Bohr's parents married in 1881."

# pattern = r'[a-zA-Z]+\.'
# result = re.findall(pattern, string)
# print(result)


# pattern = r'\s+'
# result = re.findall(pattern, string)
# words = re.split(pattern, string)
# print("words: ", words)


# pattern = r"\d+\-+\d+"
# result = re.findall(pattern, string)
# print(result)


pattern = r",|\-"
words = re.split(pattern, string)
print("words: ", words)