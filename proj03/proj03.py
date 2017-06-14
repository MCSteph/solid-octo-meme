# Name:
# Date:


""" 
proj 03: Guessing Game

Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, 
or exactly right. Keep the game going until the user types exit.
Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""
import random
var = random.randint(1,10)
name = raw_input("whats your name? ")
if name == "Chad":
    user_input = int(raw_input("guess a number between 1 and 10 "))
    print "Congradulations! You guessed correctly!"
    pass
elif name == "Abinav" or name == "Beckey" or name == "Cheesecake":
    user_input2 = int(raw_input("guess a number between 1 and 10 "))
    long = int(raw_input("guess a number between 1 and 10 "))
    if long == "5256005256005256005256005256005256005256005256005256005256005256005256005256005256005256001234567890":
        print "wow... i didnt expect you do guess that... welp i guess you deserve this..."
        print "Congradulations! You guessed correctly!"
        print "."
        print "."
        print "."
        print "JK U SUCK!!!!!"
    else:
        print "Your wrong, and you dont get another try because your a bad person"
    pass
else:
    user_input = int(raw_input("guess a number between 1 and 10 "))
    unum = user_input
    if unum == var:
        print "Congradulations! You guessed correctly!"
    else:
        print "sorry, only two more tries "
        user_input = int(raw_input("guess again "))
        unum = user_input
        if unum == var:
                print "Congradulations! You guessed correctly!"
        else:
                print "sorry, only one more try"
                user_input = int(raw_input("guess again "))
                unum = user_input
                if unum == var:
                    print "Congradulations! You guessed correctly!"
                else:
                    print "sorry, your out of tries"

