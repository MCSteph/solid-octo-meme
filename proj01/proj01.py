
# Date:

# proj01: A Simple Program
# This program asks the user for his/her name and age.
# Then, it prints a sentence that says when the user will turn 100.

# If you complete extensions, describe your extensions here!


user_input1 = raw_input("What is your name? ")
name = user_input1
Cheesecake = name
Abinav = name + Cheesecake
if name == Cheesecake or name == Abinav:
    print "you don't get an age or get to see any movies... nerd"
else:
    pass
    user_input2 = raw_input("What year were you born? ")
    user_input3 = raw_input("have you had a birthday this year?")
    years = int(user_input2) + 100
    print "You will be 100 in " + str(years)
    age = 2017 - int(user_input2)
    if age > 17:
        print "and you may view all movie ratings"
    if age == 17:
        print "and you may view G, PG, PG-13, and R movies"
    if age < 17 and age >= 13:
        print "and you may view G, PG, and PG-13 movies"
    if age <= 12:
        print "and you may view G and PG movies"
