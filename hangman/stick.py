def stick4():   
    a_file = open("stickman.txt")
    lines_to_read = [0,1,2,3,4,5,6]

    for position, line in enumerate(a_file):
        if position in lines_to_read:
            print(line)

def stick3():   
    a_file = open("stickman.txt")
    lines_to_read = [8,9,10,11,12,13,14]

    for position, line in enumerate(a_file):
        if position in lines_to_read:
            print(line)

def stick2():   
    a_file = open("stickman.txt")
    lines_to_read = [16,17,18,19,20,21,22]

    for position, line in enumerate(a_file):
        if position in lines_to_read:
            print(line)

def stick1():   
    a_file = open("stickman.txt")
    lines_to_read = [24,25,26,27,28,29,30]

    for position, line in enumerate(a_file):
        if position in lines_to_read:
            print(line)