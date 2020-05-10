#Imputed Numbers to choose the highest from
Number1 = input("choose Number1:")
Number2 = input("choose Number2:")
Number3 = input("choose Number3:")

#Figureing our the highest Number

#Checking if Number1 is the hignhest
if Number1>Number2 and Number1>Number3:
    print("Hingest number is {}".format(Number1))
#Checking if Number2 is the hignhest
elif Number2>Number1 and Number2>Number3:
    print("Hingest Number is {}".format(Number2))
#Checking if Number3 is the hignhest
elif Number3>Number1 and Number3>Number2:
    print("Hingest Number is {}".format(Number3))
#Checking if all numbers are the same
elif Number3==Number1==Number2:
    print("All Numbers are the same")
