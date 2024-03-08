def test():
    tempo, answer = [], 0
    with open(PATH + text_file, 'r') as file:
        for line in file:
            if len(tempo) < 5:
                tempo.append(line)
            else:
                break
    
    for line in tempo:
        print(line, end ="")
        num1 = num2 = 0
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

        print(f"{num1} + {num2} = {num1 + num2}")
        answer = answer + int(num1 + num2)
    
    print(answer)