import random
import string


#defines a size to the crypt
size=16

#Admin bypass
admCrypt = "Admin@123"


#Get text to encrypty
entercrypt = input("enter your text to encrypt: ")
#Creates a cryptography
genCrypt= ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(size))
#saves the cryptography.
with open("cryptography.txt", "w") as save:
    save.write( entercrypt + " = " + genCrypt)
    save.close

#count error parameter.
countError = 1
while countError <= 3:
    #decrypt the text
    toDecrypt = input("enter the parameter to decrypt: ")
    if toDecrypt == genCrypt or toDecrypt == admCrypt:
        print("heres your text: " + entercrypt)
        break
    else:
        countError = countError+1
        print("The Crypt does not exist.")
        
        






        
        
    
    

