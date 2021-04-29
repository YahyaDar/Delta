import string
import random

LETTERS = string.ascii_letters
NUMBERS = string.digits  
PUNCTUATION = string.punctuation    

def get_password_length():
    '''
      Retrieves the length of a password
      :returns number <class 'int'>
    '''
    length = input("How long do you want your password: ")
    return int(length)

def password_generator(cbl, length=8):
    '''
    Generates a random password having the specified length
    :length -> length of password to be generated. Defaults to 8
        if nothing is specified
    :cbl-> a list of boolean values representing a user choice for 
        string constant to be used to generate password.
        0th list item represents digits    
             True to add digits to constant False otherwise
        1st list item represents letters   
             True to add letters to constant False otherwise
        2nd list item represents punctuation
             True to add punctuation to constant False otherwise
    :returns string <class 'str'>
    '''
        # create alphanumerical from string constants
    printable = f'{LETTERS}{NUMBERS}{PUNCTUATION}'

    # convert printable from string to list and shuffle
    printable = list(printable)
    random.shuffle(printable)

    # generate random password and convert to string
    random_password = random.choices(printable, k=length)
    random_password = ''.join(random_password)
    return random_password

    # create alphanumerical by fetching string constant
    printable = fetch_string_constant(cbl)

