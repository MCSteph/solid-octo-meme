
# Date:

# proj01: A Simple Program
# This program asks the user for his/her name and age.
# Then, it prints a sentence that says when the user will turn 100.

# If you complete extensions, describe your extensions here!


user_input1 = raw_input("What is your name? ")
name = user_input1
if name == "Cheesecake" or name == "Abinav" or name == "Beckey":
    print "You don't deserve to get a year or watch movies... nerd"
    user_input2 = raw_input("Do you have anything to say for yourself? ")
    sorry = user_input2
    if sorry == "im sorry":
        print "really? ... Well i guess i can forgive you"
    if sorry == "i want to die":
        print "THEN DO IT!"
        user_input3 = raw_input("... how can you prove it to me? ")
        prove = user_input3
        if prove == "by taking the test under a different name":
            print "ok, i hope you told the truth"
        if prove == "i dont know":
            print "then you need to... DIE!!"

else:
    user_input4 = raw_input("What year were you born? ")
    user_input5 = raw_input("have you had a birthday this year? ")
    years = int(user_input4) + 100
    print "You will be 100 in " + str(years)
    age = 2017 - int(user_input4)
    if age > 17:
        print "and you may view all movie ratings"
    if age == 17:
        print "and you may view G, PG, PG-13, and R movies"
    if age < 17 and age >= 13:
        print "and you may view G, PG, and PG-13 movies"
    if age <= 12:
        print "and you may view G and PG movies"
