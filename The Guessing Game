print("The Guessing Game")
import random
x=random.randint(1,20)
attempt=1
print("Guess a number between 1-20")
while (attempt<6):
    guess = input ("Guess...")
    g1 = int(guess)
    if g1==x:
        break
    elif x>g1:
        print("Guess should be greater...")
        attempt = attempt + 1
    else:
        print("Guess should be smaller...")
        attempt = attempt + 1
if(x==g1):
    print("CONGRATULATIONS!")
    print("Game Won in",attempt,"Attempts")
else:
    print("No Attempts Remaining")
    print("Game Over!")
