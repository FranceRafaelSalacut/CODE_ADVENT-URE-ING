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

def do_box(U_input, index1, index):
    # Naming the sides. 
    top_line = index1-1
    bottom_line = index1+1
    first_index = index
    last_index = index

    print()
    # Checking the top 
    if index1 != 0:
        #top-left
        if first_index != 0:
            print(U_input[top_line][first_index-1], end="")
        else:
            print(end="")
        #direct-top
        print(U_input[top_line][index], end="")
        #top-right
        if last_index != len(U_input[index1])-1:
            print(U_input[top_line][last_index + 1])
        else:
            print()

    # Checking sides
    #left
    if first_index != 0:
        print(U_input[index1][first_index-1], end="")
    else:
            print(end="")

    print(U_input[index1][index], end="")
    #right
    if last_index != len(U_input[index1])-1:
        print(U_input[index1][last_index+1])
    else:
        print()

    # Checking the bottom
    if index1 != len(U_input)-1:
        #bottom-left
        if first_index != 0:
            print(U_input[bottom_line][first_index-1], end="")
            
        #direct-bottom
        print(U_input[bottom_line][index], end="")
        #bottom-right
        if last_index != len(U_input[index1])-1:
            print(U_input[bottom_line][last_index + 1])
        else:
            print()

    print()
    

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
            slot = get_number(U_input,top_line, first_index-1, False)
            if slot not in number:
                number.append(slot)
        #direct-top
        if U_input[top_line][index].isnumeric():
            slot = get_number(U_input,top_line, index, False)
            if slot not in number:
                number.append(slot)

        #top-right
        if U_input[top_line][last_index + 1].isnumeric() and last_index != len(U_input[index1])-1:
            slot = get_number(U_input,top_line, last_index+1, False)
            if slot not in number:
                number.append(slot)
        
    # Checking the bottom
    if index1 != len(U_input)-1:
        #bottom-left
        if U_input[bottom_line][first_index-1].isnumeric() and first_index != 0:
            slot = get_number(U_input,bottom_line, first_index-1, False)
            if slot not in number:
                number.append(slot)

        #direct-bottom
        if U_input[bottom_line][index].isnumeric():
           slot = get_number(U_input,bottom_line,index, False)
           if slot not in number:
                number.append(slot)

        #bottom-right
        if U_input[bottom_line][last_index + 1].isnumeric() and last_index != len(U_input[index1])-1:
            slot = get_number(U_input,bottom_line,last_index+1, False)
            if slot not in number:
                number.append(slot)
        
    # Checking sides
    #left
    if first_index != 0:
        if U_input[index1][first_index-1].isnumeric():
            number.append(get_number(U_input,index1,index-1, False))

    #right
    if last_index != len(U_input[index1])-1:
        if U_input[index1][last_index+1].isnumeric():
            number.append(get_number(U_input,index1,index+1, False))

    #ic(number)
    #do_box(U_input, index1, index)
    #test = input()
    #time.sleep(0.1)
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
                #ic(f"{index1+1}")
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