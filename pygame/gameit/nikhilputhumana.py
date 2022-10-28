# NUMBER GUESSING GAME
# User can guess a random number between 1 and 100.
# Each game has 10 chances and for each chance missed, the points will be decremented by 10.
# The second level consist of 5 guesses and points decrements by 20 for each wrong guess.
# Messages will be shown based on how close your guess is.
# The aim is to find the number with least number of guesses.

import random

def numberGuessingGame():
    print('\n\t\tWELCOME to this NUMBER GUESSING GAME! \n\n You have 10 chances to guess the number, \n You have 100 points and each guess decrements 10 points \n \n \t\tCOMEON LETS START!!!!')
    name=input('\nEnter your name: ')
    x=random.randint(0,100)
    point1=0
    point2=0
    count=10
    level=1
    while count>0:
        while True:
            n=input('Guess the number: ')
            try:
                n=int(n)
                break
            except ValueError:         #checking if integer or not
                print('\tEnter a valid number and try again')
        d=int(x-n)
        if x==n:
            print('\t\tCongrats', name ,'you guessed it correctly!')
            point1=count*10
            print('\t\t\tYou got',point1,'points!')
            level+=1
            break
        else :
            if count>1:
                if abs(d)<4 :
                    print('\t\t\tJust Miss!!')
                if d<0:
                    print('The number you have guessed is greater than real number, try again!')
                else:
                    print('The number you have guessed is less than real number, try again!')
                count-=1
                print('\t\t\tYou have', count , 'guesses left')
                if count==5:
                    print('\tYour points has been reduced to half! Play wisely')
                if count==2:
                    print('\tBe careful, game is going to end soon!')
            else:
                print('\t Oops!! THE GAME IS OVER!! Better luck next time. \n\t\t The number was',x)
                break
    if level==2:                 #LEVEL 2 STARTS
        print('\n\n\t\t\tLEVEL 2 \n\n\t In this level you have 5 chances to guess the number, \n\t You have 100 points and each guess decrements 20 points\n\n \t\t\t LET\'S START')
        x=random.randint(0,100)                                            
        count=5
        while count>0:
            while True:
                n=input('\nGuess the number: ')
                try:
                    n=int(n)
                    break
                except ValueError:
                    print('\tEnter a valid number and try again')
            d=int(x-n)
            if x==n:
                print('\t\tCongrats', name ,'you guessed it correctly!')
                point2=count*20
                print('\t\t\tYou got',point2,'points!')
                level+=1
                break
            else :
                if count>1:
                    if abs(d)<=3 :
                        print('\t\t\tJust Miss!!')
                    if d<0:
                        print('The number you have guessed is greater than real number, try again!')
                    else:
                        print('The number you have guessed is less than real number, try again!')
                    count-=1
                    print('\t\t\tYou have', count , 'guesses left\n')
                    if count==2:
                        print('\tBe careful, game is going to ends soon!')
                else:
                    print('\t Oops!! THE GAME IS OVER!! Better luck next time. \n\t\t The number was',x)
                    break
        print('\n\t\tYou scored a total of',point1+point2,'points\n')

