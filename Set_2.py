#!/usr/bin/env python
# coding: utf-8

# In[16]:


def shift_letter(letter, shift):
    
    letter_shift_map = {' ':0, 'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
    shift_letter_map = {0:' ', 1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H', 9:'I', 10:'J', 11:'K', 12:'L', 13:'M', 14:'N', 15:'O', 16:'P', 17:'Q', 18:'R', 19:'S', 20:'T', 21:'U', 22:'V', 23:'W', 24:'X', 25:'Y', 26:'Z'}
    if str(letter) == " ":
        shifted_letter = " "
    else:
        letter_value = int(letter_shift_map[str(letter)])+int(shift)
        while letter_value > 26:
            letter_value = letter_value - 26
        shifted_letter = shift_letter_map[int(letter_value)]
    return(shifted_letter)

def caesar_cipher(message, shift):
    loop=0
    end=len(message)-1
    new_message=''
    value_map = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
    letter_map = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H', 9:'I', 10:'J', 11:'K', 12:'L', 13:'M', 14:'N', 15:'O', 16:'P', 17:'Q', 18:'R', 19:'S', 20:'T', 21:'U', 22:'V', 23:'W', 24:'X', 25:'Y', 26:'Z'}
    while loop<=end:
        letter=message[loop]
        if letter ==' ':
            new_letter=' '
        else:
            value=value_map[letter]
            new_value=value+shift
            while new_value > 26:
                new_value=new_value-26
            new_letter=letter_map[new_value]
        new_message = new_message+new_letter
        loop=loop+1
    return(new_message)

def shift_by_letter(letter, letter_shift):
    value_map = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
    letter_map = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H', 9:'I', 10:'J', 11:'K', 12:'L', 13:'M', 14:'N', 15:'O', 16:'P', 17:'Q', 18:'R', 19:'S', 20:'T', 21:'U', 22:'V', 23:'W', 24:'X', 25:'Y', 26:'Z'}
    if letter == ' ':
        new_letter = ' '
    else:
        value = value_map[letter]
        shift = value_map[letter_shift]-1
        new_value=value+shift
        while new_value>26:
            new_value=new_value-26
        new_letter=letter_map[new_value]
    return(new_letter)
    
def vigenere_cipher(message, key):
    loop=0
    end=len(message)-1
    new_message=''
    value_map = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
    letter_map = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H', 9:'I', 10:'J', 11:'K', 12:'L', 13:'M', 14:'N', 15:'O', 16:'P', 17:'Q', 18:'R', 19:'S', 20:'T', 21:'U', 22:'V', 23:'W', 24:'X', 25:'Y', 26:'Z'}
    while loop<=end:
        letter=message[loop]
        letter_key=key[((loop+1)%len(key))-1]
        if letter==' ':
            new_letter=' '
        else:
            value=value_map[letter]
            shift=value_map[letter_key]-1
            new_value=value+shift
            while new_value>26:
                new_value=new_value-26
            new_letter=letter_map[new_value]
        new_message=new_message+new_letter
        loop=loop+1
    return(new_message)
            
def scytale_cipher(message, shift):
    while len(message)%shift>0:
        message=message+'_'
    new_message=''
    loop=0
    while loop<(len(message)//shift):
        loop2=0
        while loop2<shift:
            new_letter=message[(loop+loop2*(len(message)//shift))]
            new_message=new_message+new_letter
            loop2=loop2+1
        loop=loop+1
    return(new_message)

def scytale_decipher(message, shift):
    new_message=''
    loop=0
    while loop<shift:
        loop2=0
        while loop2<len(message)//shift:
            new_letter=message[loop+loop2*shift]
            new_message=new_message+new_letter
            loop2=loop2+1
        loop=loop+1
    return(new_message)


# In[ ]:





# In[ ]:




