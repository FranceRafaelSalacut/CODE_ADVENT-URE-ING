from icecream import ic #for debugging

# Constants
PATH = "2023/Day 3/"
text_file = "input.txt"

temp = []
index = 0
with open(PATH + text_file, 'r') as file:
    for line in file:
        if len(temp) < 2:
            line = line.split("\n")[0]
            temp.append(line)
        else:
            break

def find_sp_symbol(input, index1, indexes):
    # Checking the top 
    if index1 != 0:
        #top-left
        if input[index1 - 1][indexes[0]-1] != '.':
            ic()
            return True
        #direct-top
        for x in indexes:
            if input[index - 1][x] != ".":
                ic()
                return True
        #top-right
        if input[index1 - 1][indexes[len(indexes)-1] + 1] != '.':
            ic()
            return True
        
    # Checking the bottom
    if index1 != len(input)-1:
        #bottom-left
        if input[index1 + 1][indexes[0]-1] != '.':
            ic()
            return True
        #direct-bottom
        for x in indexes:
            if input[index + 1][x] != ".":
                ic()
                ic(f"{x} in {indexes}")
                ic(input[index + 1][x])
                return True
        #bottom-right
        if input[index1 + 1][indexes[len(indexes)-1] + 1] != '.':
            ic()
            return True
        
    # Checking sides
    #left
    if indexes[0] != 0:
        if input[index1][indexes[0]-1] != '.':
            ic()
            return True
    #right
    if indexes[len(indexes)-1] != len(input[index1])-1:
        if input[index1][indexes[len(indexes)-1]+1] != '.':
            ic()
            return True

    ic("made it through all the hecks")
    return False

def get_answer_1(input):
    sum = []
    number = ""
    indexes = []
    found = False
    for index1, line in enumerate(input):
        for index2, symbol in enumerate(line):
            if symbol.isnumeric():
                found = True

            if found:
                if not symbol.isnumeric():
                    found = False
                    ic(number)
                    if find_sp_symbol(input, index1, indexes):
                        sum.append(number)
                    number = ""
                    indexes = []
                    continue
                number = number + symbol
                indexes.append(index2)
            

    return sum

def main():
    for x in temp:
        print(x)
    sum = get_answer_1(temp)
    print(sum)

if __name__ == '__main__':
	main()