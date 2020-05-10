import random

rl = random.randint(1,6)
print("Do you want to roll the dice?\n")
print("YES / NO")
r = input()
if r=='yes':
    g = int(input("what is your number\n"))
    while r == "yes" or "y":
        print("Rolling...")
        print('number is')
        print(rl)
        break
    if g == rl:
        print("Yes.its correct\n")
    else:
        print("No,its not correct!\n")
if r == 'no':
    print('NO DICE FOR YOU\n')