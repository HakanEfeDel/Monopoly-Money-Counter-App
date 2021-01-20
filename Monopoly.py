#   MONOPLY BANK ACOUNT KEEPER   #

from array import *

while True:
    try:
        money = int(input("How much money will each player start with? "))
        break
    except ValueError:
        print("Please typee only numbers.")
    

correctInput = False 

while not correctInput:

    while True:
        try:
            #It takes the number of players.
            pN = int(input("How many players will play? "))
            break
        except ValueError:
            print("Please typee only numbers.")    


    #It looks if the player numbers are in the range.
    if pN>=2 and pN<=6:
        #It creates a bank account for each player.
        playersBank = []
        correctInput = True

    #It leads to the step that prints what prints if the number of players are out of range.
    else:
        #Prints what it should do.
        print("This is not a valid number please choose a number between 2 and 6.")

#It asks the names of all the plaeyrs.            
for i in range(pN):
    #It prints the quesion that asks the names of all players in order.
    print(i+1, ". player's name? ")
    #This is the
    temp = input()
    playersBank.insert(i, [temp, money])

for r in playersBank:
    print(r[0], "has", r[1], "$.")
    

    
print("Please put transactions in the format below.")
print("<Payers Name> <space> <Takers Name> <Space> <Amount>")
print("Example 1: Jack bank 500")
print("Example 2: Bob Jack 50")
while True:
    transaction = input("Please type the transaction. ")
    transaction1 = transaction.split()
    print(transaction1[0], transaction1[1])

    payerFound = False
    takerFound = False

    for r in playersBank:
        if transaction1[0] in r[0] or transaction1[0] == "bank":
            payerFound = True
            while True:
                try:
                    if transaction1[0] == "bank":
                        pass
                    else:
                        r[1] = r[1] - int(transaction1[2])
                    break
                except ValueError:
                    print("Please type a avaliable transaction type.")
                    break


        if transaction1[1] in r[0] or transaction1[1] == "bank":
            takerFound = True
            while True:
                try:
                    if transaction1[1] == "bank":
                        pass
                    else:
                        r[1] = r[1] + int(transaction1[2])
                    break
                except ValueError:
                    print("Please type a avaliable transaction type.")
                    break

 
    if payerFound and takerFound:
        print("Player and taker is found in the array.")
    else:
        print("Please type a avaliable transaction type.")
    for r in playersBank:
        print(r[0], "has", r[1], "$.")
        
