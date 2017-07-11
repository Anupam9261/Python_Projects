print('Welcome to Hangman')
import random
hangman=["""
  _____________
  |     |     |
  |           |
  |           |
 _|_         _|_
|___|       |___|
""","""
  _____________
  |     |     |
  |     O     |
  |           |
 _|_         _|_
|___|       |___|
""","""
  _____________
  |     |     |
  |     O     |
  |     |     |
 _|_         _|_
|___|       |___|
""","""
  _____________
  |     |     |
  |     O     |
  |    /|     |
 _|_         _|_
|___|       |___|
""","""
  _____________
  |     |     |
  |     O     |
  |    /|\    |
 _|_         _|_
|___|       |___|
""","""
  _____________
  |     |     |
  |     O     |
  |    /|\    |
 _|_   /     _|_
|___|       |___|
""","""
  _____________
  |     |     |
  |     O     |
  |    /|\    |
 _|_   / \   _|_
|___|       |___|
"""]
words="india china japan london paris".split()

def randomwords(words):
    index = random.randint(0 , len(words) - 1)
    return (index)

missedletter = ""
correctletter = ""
sword = randomwords(words)
secretword = words[sword]
gameisdone = False

def displayboard(hangman, missedletter, correctletter, secretword):
    print (hangman[len(missedletter)])
    for letter in missedletter:
        print (" Missed Letter ", letter)
    blanks = "_" *len(secretword)
    for i in range(len(secretword)):
        if(secretword[i] in correctletter):
            blanks = blanks[:i] + secretword[i] + blanks[i+1:]
    for letter in blanks:
       print(letter, end=" ")

def getguess(alreadyguess):
    guess = input (" Enter a letter")
    print("")
    print("")
    guess = guess.lower()
    if (len(guess)!=1):
        print(" Enter only one letter")
        return(guess)
    elif (guess not in "abcdefghijklmnopqrstuvwxyz"):
        print(" Please Enter Only Alphabets")
        return(guess)
    elif (guess in alreadyguess):
        print(" Already Entered")
        return(guess)
    else:
        return(guess)

def playagain():
    play = input (" Do you want to play again??? (y/n)")
    play = play.lower()
    if (play=="y"):
        print (" Play Again")
        return(True)
    else:
        print (" Quit")
        return(False)
        
while True:
    displayboard(hangman, missedletter, correctletter, secretword)
    guess = getguess (missedletter + correctletter)
    if (guess in secretword):
        correctletter = correctletter + guess
        foundallletter = True
        for i in range(len(secretword)):
            if (secretword[i] not in correctletter):
                foundallletter = False
                break
        if (foundallletter == True):
            print (" ",secretword)
            print (" You Win")
            gameisdone = True
    else:
        missedletter = missedletter + guess
        if (len(missedletter) == len(hangman) - 1):
            displayboard(hangman, missedletter, correctletter, secretword)
            print(" You have no guesses left")
            print(" Total Letter",str(len(secretword)))
            print(" Correct Letter",str(len(correctletter)))
            gameisdone = True
    if (gameisdone):
        if (playagain()):
            missedletter = ""
            correctletter = ""
            gameisdone = False
            sword = randomwords(words)
            secretword = words[sword]
        else:
            print(" Thank You for Playing")
            break
