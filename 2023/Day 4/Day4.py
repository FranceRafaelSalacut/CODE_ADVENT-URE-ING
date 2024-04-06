from icecream import ic
import os
'''
https://stackoverflow.com/questions/2582911/how-to-check-if-a-list-is-contained-inside-another-list-without-a-loop
https://stackoverflow.com/questions/43102861/finding-an-element-from-one-list-in-another-list-in-python
'''

# Constants
PATH = "2023/Day 4/"
text_file = "input.txt"


index = 0

def fill_temp():
    temp = []
    with open(PATH + text_file, 'r') as file:
        for line in file:
            #if len(temp) < 20:
                line = line.split("\n")[0]
                temp.append([line, 1])
            #else:
            #  break

    return temp

def answer_1():
    answer = 0
    with open(PATH + text_file, 'r') as file:
        for line in file:
            #if len(temp) < 2:
                #print(line)
                line = line.split("\n")[0]
                line = line[10:]
                Winning_numbers = line.split("|")[0].split()
                Drawn = line.split("|")[1].split()
                count = 0
                for x in Drawn:
                    if x in Winning_numbers:
                        count+=1

                if count != 0: answer = answer + 2**(count-1) 
            #else:
            #    break
        
    return answer


def print_given(item):
    for x in range(0,10):
        print(item[x])

def get_win(card):
    Winning_numbers = card.split("|")[0].split()
    Drawn = card.split("|")[1].split()
    count = 0
    for x in Drawn:
        if x in Winning_numbers:
            count+=1

    return count

def answer_2():
    answer = 0
    cards = fill_temp()
    for index,x in enumerate(cards):
        card = x[0][10:]
        #print(index+1)
        #ic(get_win(card))
        multiplyer = x[1]
        lower_bound = index+1
        upper_bound = index+get_win(card)+1
        for y in range(lower_bound, upper_bound):
            if y < len(cards):
                cards[y][1]+=1*multiplyer
        #print_given(cards[index:])
        #ic(len(cards))
        #t = input()
        #os.system("cls")
    
    for x in cards:
         answer = answer + x[1]

    return answer

        
def main():
    print(answer_1())
    print(answer_2())

if __name__ == '__main__':
	main()