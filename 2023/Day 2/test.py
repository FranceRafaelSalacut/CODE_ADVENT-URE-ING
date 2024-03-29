PATH = "2023/Day 2/"
text_file = "input.txt"
red, green, blue = 0,0,0


temp = []
with open(PATH + text_file, 'r') as file:
    for line in file:
        if len(temp) < 1000:
            temp.append(line)

answer = 0
for line in temp:
    red, green, blue = 0,0,0
    line = line.split("\n")[0]

    Game_No = line.split(":")[0]#.split()[1]
    #print(f"{Game_No} ::")

    Draws = line.split(":")[1].split(";")
    
    for Draw in Draws:
        Draw = Draw.split(",")
        for Pair in Draw:
            Number, Color = Pair.split()
            Number = int(Number)
            if Color == "red":
                if Number > red:
                    red = Number
            elif Color == "green":
                if Number > green:
                    green = Number
            elif Color == "blue":
                if Number > blue:
                    blue = Number

    print(f"{red}*{green}*{blue}")