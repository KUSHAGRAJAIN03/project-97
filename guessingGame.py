import random
x ="guess a number between 1 and 9" 
print(x)
chances=0

while chances<5:
    y =int(input("guess the number:"))
    z = random.randint(1,9)
    if y==z :
        print("YOU WON")
        break

    if y!=z :
        print("try again!")
        chances=chances+1
     
    
    if not chances<5 :
        print("YOU LOST THE NUMBER WAS",z)

    