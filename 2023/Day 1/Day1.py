'''
Resources
https://www.geeksforgeeks.org/python-extract-numbers-from-string/
https://stackoverflow.com/questions/7961499/best-way-to-loop-over-a-python-string-backwards
https://www.geeksforgeeks.org/usage-of-__main__-py-in-python/
'''

# Constants
PATH = "2023/Day 1/"
text_file = "input.txt"
spell_numbers = [
    'zero', 'one', 'two', 'three', 'four', 
    'five', 'six', 'seven', 'eight', 'nine'
]

dict_numbers = {
    'zero': '0','one' : '1', 'two' : '2', 'three': '3', 'four': '4', 
    'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
}

def find_spelled(line):
    for word in spell_numbers:
        if word in line:
            return dict_numbers[word]
    
    return False

def get_answer():
    answer = 0
    with open(PATH + text_file, 'r') as file:
        for line in file:
            temp = ""
            for char in line:
                if char.isnumeric():
                    num1 = char
                    break
                else:
                    temp = temp + char
                    found = find_spelled(temp)
                    if found != False:
                        num1 = found
                        break
                        
            temp = ""
            for char in reversed(line):
                if char.isnumeric():
                    num2 = char
                    break
                else:
                    temp = char + temp
                    found = find_spelled(temp)
                    if found != False:
                        num2 = found
                        break

            #print(f"{num1} + {num2} = {num1 + num2}")
            answer = answer + int(num1 + num2)

    return str(answer)



def main():
    test()
    #print(get_answer())

if __name__ == '__main__':
	main()
  
