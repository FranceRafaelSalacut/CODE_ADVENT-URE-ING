from icecream import ic #for debugging
import os
#ic.disable()

# Constants
PATH = "2023/Day 3/"
text_file = "input.txt"

temp = []
index = 0
with open(PATH + text_file, 'r') as file:
    for line in file:
        if len(temp) < 5:
            line = line.split("\n")[0]
            temp.append(line)
        else:
            break

def print_given():
    for x in temp:
        print(x)

def do_box(U_input, index1, indexes):
    # Naming the sides. 
    top_line = index1-1
    bottom_line = index1+1
    first_index = indexes[0]
    last_index = indexes[len(indexes)-1]

    print()
    # Checking the top 
    if index1 != 0:
        #top-left
        print(U_input[top_line][first_index-1], end="")
        #direct-top
        for x in indexes:
            print(U_input[top_line][x], end="")
        #top-right
        print(U_input[top_line][last_index + 1])

    # Checking sides
    #left
    if first_index != 0:
        print(U_input[index1][first_index-1], end="")

    for x in indexes:
            print(U_input[index1][x], end="")
    #right
    if last_index != len(U_input[index1])-1:
        print(U_input[index1][last_index+1])

    # Checking the bottom
    if index1 != len(U_input)-1:
        #bottom-left
        print(U_input[bottom_line][first_index-1], end="")
        #direct-bottom
        for x in indexes:
            print(U_input[bottom_line][x], end="")
        #bottom-right
        print(U_input[bottom_line][last_index + 1])

    print()

def find_sp_symbol(U_input, index1, indexes):
    # Naming the sides. 
    top_line = index1-1
    bottom_line = index1+1
    first_index = indexes[0]
    last_index = indexes[len(indexes)-1]
    # Checking the top 
    if index1 != 0:
        #top-left
        if U_input[top_line][first_index-1] != '.':
            ic("top_left")
            return True
        #direct-top
        for x in indexes:
            if U_input[top_line][x] != ".":
                ic(f"direct_top {x}")
                return True
        #top-right
        if U_input[top_line][last_index + 1] != '.':
            ic("top_right")
            return True
        
    # Checking the bottom
    if index1 != len(U_input)-1:
        #bottom-left
        if U_input[bottom_line][first_index-1] != '.':
            ic("bot_left")
            return True
        #direct-bottom
        for x in indexes:
            if U_input[bottom_line][x] != ".":
                ic(f"direct_bot {x}")
                return True
        #bottom-right
        if U_input[bottom_line][last_index + 1] != '.':
            ic("bot_right")
            return True
        
    # Checking sides
    #left
    if first_index != 0:
        if U_input[index1][first_index-1] != '.':
            ic("left")
            return True
    #right
    if last_index != len(U_input[index1])-1:
        if U_input[index1][last_index+1] != '.':
            ic("right")
            return True

    ic("made it through all the hecks")
    return False

def get_answer_1(U_input):
    sum = []
    number = ""
    indexes = []
    found = False
    print_given()
    for index1, line in enumerate(U_input):
        for index2, symbol in enumerate(line):
            if symbol.isnumeric():
                found = True

            if found:
                if not symbol.isnumeric():
                    found = False
                    do_box(U_input, index1, indexes)
                    ic(number)
                    if find_sp_symbol(U_input, index1, indexes):
                        sum.append(int(number))
                    number = ""
                    indexes = []
                    test = input()
                    os.system('cls')
                    print_given()
                    continue
                number = number + symbol
                indexes.append(index2)
            

    return sum

def main():
    sam = get_answer_1(temp)
    print(sum(sam))

if __name__ == '__main__':
	main()