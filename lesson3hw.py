import random

playagain = True

while playagain:
    num = random.randint(1,20)
    count = 0
    print("You have only '5' chance to guess number")

    while count < 5:
        number = int(input("please enter 1~20 :"))
        count = count + 1

        if num == number:
            print("You are right!")
            print("You have guessed %d times" % count )
            break
        elif number > num:
            print("Your number is bigger than the answer!")
        
        elif number < num:
            print("Your number is smaller than the answer!")
        

    print("You failed the challange")
    answer = input ("Do you want to play again? (yes/no) :")
    
    if answer == "yes":
        playagain = True
    elif answer == "no":
        playagain = False
    
    





    

