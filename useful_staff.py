from math import sqrt
import numpy as np
import random



def processInput(primes):
    if (isPrime(primes)):
        return primes
        #print(primes)
    else:
        while(isPrime(primes) is False):
            primes += 1
            #print(primes)
        return primes




def isPrime(n):
    if n < 1:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True




def genKeys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    # choose e
    # e is co-prime with phi & 1 < e <= phi
    while True:
        e = random.randrange(2 ** (p - 1), 2 ** q - 1)
        if (isCoPrime(e, phi)):
            break

    d = modInv(e, phi)  # d is mod inv of e with respect to phi, e * d (mod phi) = 1
    return e, d, n




def isCoPrime(p, q):      #return True if gcd(p, q) is 1  i.e, relatively prime
    return gcd(p, q) == 1




def gcd(p, q):      #euclidean algorithm to find gcd of p and q

    while q:
        p, q = q, p % q
    return p




def modInv(a, b):
    gcd, x, y = egcd(a, b)

    if x < 0:
        x += b

    return x




def egcd(a, b):
    s = 0
    old_s = 1
    t = 1
    old_t = 0
    r = b
    old_r = a

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t




def DixonsAlg(n):
    base = [2, 3, 5, 7]
    start = int(sqrt(n))
    pairs = []
    for i in range(start, n):
        for j in range(len(base)):  # Finding the related squares
            lhs = i ** 2 % n
            rhs = base[j] ** 2 % n
            if (lhs == rhs):
                pairs.append([i, base[j]])

    new = []
    for i in range(len(pairs)):
        factor = gcd(pairs[i][0] - pairs[i][1], n)

        if (factor != 1):
            new.append(factor)

    x = np.array(new)

    return (np.unique(x))