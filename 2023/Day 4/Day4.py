'''
https://stackoverflow.com/questions/2582911/how-to-check-if-a-list-is-contained-inside-another-list-without-a-loop
https://stackoverflow.com/questions/43102861/finding-an-element-from-one-list-in-another-list-in-python
'''

# Constants
PATH = "2023/Day 4/"
text_file = "input.txt"

temp = []
index = 0

def answer_1():
    answer = 0
    with open(PATH + text_file, 'r') as file:
        for line in file:
            if len(temp) < 2:
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
            else:
                break
        
        return answer

def main():
    print(answer_1())

if __name__ == '__main__':
	main()