
# Constants
PATH = "2023/Day 2/"
text_file = "input.txt"
red, green, blue = 12, 13, 14

def get_answer():
    Answer = 0
    with open(PATH + text_file, 'r') as file:
        for line in file:
            line = line.split("\n")[0]

            Game_No = line.split(":")[0].split()[1]

            Draws = line.split(":")[1].split(";")
            
            Pass = True
            for Draw in Draws:
                Draw = Draw.split(",")
                for Pair in Draw:
                    Number, Color = Pair.split()
                    Number = int(Number)
                    if Color == "red":
                        if Number > red:
                            Pass = False
                            break
                    elif Color == "green":
                        if Number > green:
                            Pass = False
                            break
                    elif Color == "blue":
                        if Number > blue:
                            Pass = False
                            break
            
            if Pass:
                Answer = Answer + int(Game_No)
    
    print(Answer)

def main():
    #test()
    get_answer()

if __name__ == '__main__':
	main()