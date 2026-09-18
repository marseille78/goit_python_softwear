import re

string = "Niels Bohr was born to Christian Bohr (1858-1911), a professor of physiology at the University of Copenhagen,"\
         "twice a candidate for the Nobel Prize in physiology and medicine,[10] and Ellen Adler (" \
         "1860-1930), daughter of the influential and very wealthy Jewish banker and liberal parliamentarian David " \
         "Baruch Adler (1826—1878) and Jenny Raphael (1830-1902) of the British Jewish " \
         "Raphael Raphael & sons[en][11] of the British Jewish banking dynasty. Bohr's parents married in 1881."

# pattern = r'[0-9]+'
pattern = r'\w+\.$'


# re.search
# result = re.search(pattern, string)
# print(result.span())
# first, last = result.span()
# print(string[first:last])



result = re.findall(r"\d{4}", string)
print("findall: ", result)