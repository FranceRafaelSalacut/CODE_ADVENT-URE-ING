# Constants
PATH = "2023/Day 3/"
text_file = "input.txt"

temp = []
with open(PATH + text_file, 'r') as file:
    for line in file:
        if len(temp) < 5:
            temp.append(line)
        else:
            break

print(temp)