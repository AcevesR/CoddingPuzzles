import string
from random import choice, shuffle

#We are going to create a random passsword generator.

def randomPassword():

    #First, we create three different lists, each one with all the possible characters of each category (lowercases, uppercases and digits).
    lower = list(string.ascii_lowercase)
    upper = list(string.ascii_uppercase)
    digits = list(string.digits)

    #We generate a list made of the three previous lists and we shuffle it, we shuffle it because originally they are created in an alphabetical order.
    all = lower + upper + digits
    shuffle(all)
    
    length = int(input("How long do you want the password?"))
    password = ''

    #Here in the for loop we ask for the length, and choice choose a random element of our 'all' list, then it does that for each character that we need.
    for i in range(length):
        password += choice(all)
    print(password)

randomPassword()
