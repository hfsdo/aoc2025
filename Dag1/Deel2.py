with open("Dag1/input.txt") as file:
    current = 50
    response = 0
    for line in file:
        amount = int(line[1:])
        if line[0] == "R":
            current += amount
        elif line[0] == "L":
            if current == 0:
                response -= 1
            current -= amount
        
        if current == 0:
            response += 1

        while current >= 100:
            current -= 100
            response += 1
        while current < 0:
            current += 100
            response += 1
            if current == 0:
                response += 1
    print({"current position":current, "code":response})

