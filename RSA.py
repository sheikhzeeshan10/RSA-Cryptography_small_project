#!/usr/bin/env python3
from useful_staff import *

def main():

    msg = input("Enter your message: ")
    primeOne = len(msg)*len(msg)+11
    printTwo = len(msg)**3+17
    p = processInput(primeOne)
    q = processInput(printTwo)

    print("p: "+str(p))
    print("q: "+str(q))

    e, d, n = genKeys(p, q)

    #print("n: " + str(n))
    #print("e: " + str(e))
    #print("d: " + str(d))

    encrypted_msg = encryption(msg,e,n)
    print("Encrypted message : " + str(encrypted_msg))
    #print("Encrypted message : "+str(encrypted_msg))

    factors = DixonsAlg(n)
    print("D_Prime 1st (i.e, p): "+str(factors[0]))
    print("D_Prime 2nd (i.e, q): "+str(factors[1]))

    decrypted_msg = decryption(d,n,encrypted_msg)
    print("decrypted message : " +str(decrypted_msg))



def encryption(msg,e,n):
    #processing message and encryption
    encrypted_msg = ""

    for c in msg:
        m = ord(c)
        encrypted_msg += str(pow(m, e, n)) + " "
    return encrypted_msg



def decryption(d,n,encrypted_msg):
    # processing Cipher-Text and Decryption
    Original_msg = ""
    parts = encrypted_msg.split()
    #print(parts)
    for part in parts:
        if part:
            c = int(part)
            #print("Co: " + str(c))
            #print("Do: " + str(d))
            #print("No: " + str(n))
            Original_msg += chr(pow(c, d, n))
    return Original_msg





if __name__ == '__main__':
    main()