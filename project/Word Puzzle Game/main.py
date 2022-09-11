'''
Problem Statement: You have to write a Word Puzzle Game in which the user has to form
the correct word out of a given set of characters. In the game the user has to solve this
puzzle for 5 words, one at a time. Problem words are stored in a list and appear to the user
in random sequence. Give the user score +1 for each correct answer and give -1 for each
wrong answer. At last print the final score. You can store any number of words in the list, but
in each round of the game only 5 words are shown to the user.

'''

import random


print("you want to play y or n:",)
select=input()

while(select=='y'):
    
    score=0
    word=["father","green","aeroplane","angle","Agree","Apple","Block"]


    def checkword(x):
        checkrandom=[]

        for same in checkrandom:
            if same==x:
                newword=random.choice(word)
                checkword(newword)
                

        checkrandom.append(x)

    for i in range(5):

        i=random.choice(word)
        checkword(i)
    

        x=list(i)

        random.shuffle(x)
        shuffleword="".join(x)

        print("Guess the word:",shuffleword)
        userinput=input("Input:")
        
        print("")


        if i==userinput:
            score+=1
        else:
            score-=1
        

    print("")
    print("Score is:",score)

    print("you want to play y or n:")
    select=input()

        



