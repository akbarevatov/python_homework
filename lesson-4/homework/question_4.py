import random
rand = random.randint(1,100)
c=9
restart = "ok"

while(restart=="ok" or restart=="Y" or restart=="yes" or restart=="y" or restart=="YES"):
    num = int(input("Start guessing: "))
    while(c>0 and num!=rand):
        if(num>rand):
            num=int(input("Too high! "))
        elif (num<rand):
            num = int(input("Too low! "))
        c-=1
    if(num==rand):
        print("You guessed it right!")
        break
    else:
        restart=input("You lost. Want to play again? ")
        c=9
        rand = random.randint(1, 100)