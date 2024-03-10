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
                tempo.append(char)
            temp.append(tempo)
        else:
            break



for x in range(0, len(temp)):
    for y in range(0, len(temp[x])):
        print(temp[x][y], end=" ")
    print("\n---------------------------------------------------------------------------")
