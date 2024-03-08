'''
Resources
https://www.geeksforgeeks.org/python-extract-numbers-from-string/
https://stackoverflow.com/questions/7961499/best-way-to-loop-over-a-python-string-backwards
'''

# Constants
PATH = "2023/Day 1/"
text_file = "input.txt"


answer = 0
with open(PATH + text_file, 'r') as file:
    for line in file:
        for char in line:
            if char.isnumeric():
                num1 = char
                break

        for char in reversed(line):
            if char.isnumeric():
                num2 = char
                break

        #print(f"{num1} + {num2} = {num1 + num2}")
        answer = answer + int(num1 + num2)


print(answer)


    
