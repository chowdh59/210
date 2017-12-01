#Question 8

binary=False                    # set this to True or False
lo,hi=1,20000               # range of the number, between 1 and 20000
 
import random as ran
 
the_num=ran.randint(lo,hi)  # computer would choose a number at random
print("I'm thinking of a number between",lo,"and",hi)
 
lo=1
hi=hi
guesses=5
 
for i in range(lo,hi):    # repeat this until guess is correct:
                                    # note the int!
#    guess=int(input ("What is your guess: ")) # uncomment to actually play
    if binary:  guess=lo+(hi-lo)//2     # integer division
    else:       guess=ran.randint(lo,hi)
    print("Guess:",guess)
    guesses+=1                      # add 1 to count of guesses
                                    # check the guessed number
    if guess > the_num:
        print("Lower!")
        hi=guess                        # bring down the upper bound
    elif guess < the_num:
        print("Higher!")
        lo=guess                        # push up the lower bound
    else: break                     
 
print("That took",guesses,"guesses")
#print("That took {5} guesses".format(guesses))
