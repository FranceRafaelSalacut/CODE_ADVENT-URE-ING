from icecream import ic #for debugging
import os
import time
#ic.disable()

# Constants
PATH = "2023/Day 3/"
text_file = "input.txt"

temp = []
index = 0
with open(PATH + text_file, 'r') as file:
    for line in file:
        #if len(temp) < 5:
            line = line.split("\n")[0]
            temp.append(line)
        #else:
        #    break

def print_given():
    for x in temp:
        print(x)

def get_number(U_input, index1, index2, reverse):
    number = ""
    while(True):
        if U_input[index1][index2].isnumeric():
            index2-=1
            if index2 == -1:
                index2+=1
                break
        else:
            index2+=1
            break

    while(True):
        if U_input[index1][index2].isnumeric():
            number = number + U_input[index1][index2]
            index2+=1
            if index2 == len(U_input[index1]):
                break
        else:
            break
    
    return number


def find_adjacent(U_input, index1, index):
    # Naming the sides. 
    number = []
    top_line = index1-1
    bottom_line = index1+1
    first_index = index
    last_index = index
    # Checking the top 
    if index1 != 0:
        #top-left
        if U_input[top_line][first_index-1].isnumeric() and first_index != 0:
            number.append(get_number(U_input,top_line, first_index-1, False))
        #direct-top
        elif U_input[top_line][index].isnumeric():
            number.append(get_number(U_input,top_line, index, False))

        #top-right
        elif U_input[top_line][last_index + 1].isnumeric() and last_index != len(U_input[index1])-1:
            number.append(get_number(U_input,top_line, last_index+1, False))
        
    # Checking the bottom
    if index1 != len(U_input)-1:
        #bottom-left
        if U_input[bottom_line][first_index-1].isnumeric() and first_index != 0:
            number.append(get_number(U_input,bottom_line, first_index-1, False))

        #direct-bottom
        elif U_input[bottom_line][index].isnumeric():
           number.append(get_number(U_input,bottom_line,index, False))

        #bottom-right
        elif U_input[bottom_line][last_index + 1].isnumeric() and last_index != len(U_input[index1])-1:
            number.append(get_number(U_input,bottom_line,last_index+1, False))
        
    # Checking sides
    #left
    if first_index != 0:
        if U_input[index1][first_index-1].isnumeric():
            number.append(get_number(U_input,index1,index-1, False))

    #right
    if last_index != len(U_input[index1])-1:
        if U_input[index1][last_index+1].isnumeric():
            number.append(get_number(U_input,index1,index+1, False))

    ic(number)
    test = input()
    os.system("cls")
    if len(number) == 2:
        return int(number[0]) * int(number[1])
    else:
        return 0

def get_answer_2(U_input):
    sum = 0
    number = []
    indexes = []
    found = False
    done = False
    #print_given()
    for index1, line in enumerate(U_input):
        for index2, symbol in enumerate(line):
            if symbol == "*":
                ic(f"{index1+1}")
                found = True

            if found:
                sum = sum + find_adjacent(U_input, index1, index2)
                found = False
            

    return sum

def main():
    sam = get_answer_2(temp)
    print(sam)

if __name__ == '__main__':
	main()