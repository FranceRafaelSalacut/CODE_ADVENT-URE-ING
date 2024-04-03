# Constants
PATH = "2023/Day 3/"
text_file = "input.txt"

temp = []
index = 0
with open(PATH + text_file, 'r') as file:
    for line in file:
        if len(temp) < 2:
            line = line.split("\n")[0]
            tempo = []
            for char in line:
                tdict = {}
                tdict[char] = False
                tempo.append(tdict)
            temp.append(tempo)
        else:
            break



for x in temp:
    print(x)
