from stick import stick4
from stick import stick3
from stick import stick2
from stick import stick1

print("____________________________")
word = input("Enter a word:\n")
print("____________________________")
guesses = ""
turns = 5
wrong = []
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char),
        else:
            print("_"),
            failed += 1
    if failed == 0:
        print("win")
        break
    guess=input("guess a letter:")    
    guesses += guess
    if guess not in word:
        wrong.append(guess)
        turns -= 1
        print("wrong")
        print("you have ", +turns, "more guesses")
        if turns == 4:
            stick4()
        elif turns == 3:
            stick3()    
        elif turns == 2:
            stick2() 
        elif turns == 1:
            stick1() 
        if turns == 0:
            print("lose")   
    print("wrong letters:")
    print(wrong)