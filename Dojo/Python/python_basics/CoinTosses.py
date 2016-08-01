
#Coin Toss
#You're going to create a program that simulates tossing a coin 5,000 times. Your program should display how many times the head/tail appears.



# i in range(1,5000):

#random import

import random

def	coin_toss():
    count = 0
    countH = 0
    countT = 0

    for i in range(1,5001):
        count += 1
        toss = round(random.random())
        if (toss == 1):
            countH += 1
            print "Attempt #" + str(count) + ": Throwing a coin... It's a head! ... Got " + str(countH) + " head(s) so far and " + str(countT) + " tail(s) so far"
        else:
            countT += 1
            print "Attempt #" + str(count) + ": Throwing a coin... It's a tail! ... Got " + str(countH) + " head(s) so far and " + str(countT) + " tail(s) so far"

    print "Ending the program, thank you!"

coin_toss()


    #if grade >= 60 and grade <= 69:
        #print ("Score: " + str(grade) + "; Your grade is D")


