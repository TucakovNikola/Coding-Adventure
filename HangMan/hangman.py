#hangman project

# entering a word and splitting it into a list
word = input(str("Enter a word\n"))

list = list(word)
print(list)

#number of tries
tries = len(list)
print(tries)

#checking the character of the list
turns = 0
#while turns <= tries:
for turns in range(tries):
    print("u have {} of tries".format(tries))
    #guessing
    guess=input(str("guess a letter\n"))
    if guess in list:
        turns +1
        print("SUCCESS")
    elif guess not in list:
        print("WRONG!")

