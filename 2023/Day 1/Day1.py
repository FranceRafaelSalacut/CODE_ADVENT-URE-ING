'''
Resources
https://www.geeksforgeeks.org/python-extract-numbers-from-string/
https://stackoverflow.com/questions/7961499/best-way-to-loop-over-a-python-string-backwards
'''

# Constants
PATH = "2023/Day 1/"
text_file = "input.txt"


temp = []

with open(PATH + text_file, 'r') as file:
    for line in file:
        temp.append(line)

sum = 0
for x in range(0,5):
    print(temp[x])
    num1 = num2 = 0
    for char in temp[x]:
        if char.isnumeric():
            num1 = int(char)
            break

    for char in reversed(temp[x]):
        if char.isnumeric():
            num2 = int(char)
            break
    
    print(f"{num1} + {num2} = {num1 + num2}")
