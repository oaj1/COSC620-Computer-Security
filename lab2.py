import string
def decrypt (k):
    
    shift =  k % 26 #k should be the int to modify ouput
    shift = -1 *shift
    cipher =  "PHHWPHDIWHUWKHWRJDSDUWB" #cipher text to decrypt
    cipher = cipher.lower() #cipher text
    alphabet = string.ascii_lowercase #alphabet to compare to 
    
    shifted = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet,shifted)#this should provide the shifted message

    newMessage = cipher.translate(table)
    
    x= print(newMessage)

    
    return x
x = 1    
while x <= 25:
    decrypt(x)
    x+=1
