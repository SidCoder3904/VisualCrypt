import random

base = 7
p = 503855227731518752419232924507       

def priv():
    priv_key=random.randint(1e100,9e100)
    return priv_key

def mod(a, b, n) : #a**b%n
    md = a%n
    if b==1 :
        return md
    r = mod(a, b//2, n)
    if b%2 :
        md = (md * r**2)%n
    else :
        md = (r**2)%n
    return md

def GenPrime() :
    while True :
        n = random.randint(100000, 999999)
        if not n%2 :
            continue
        isPrime = True
        for i in range(100) :
            a = random.choice([j for j in range(2, n)])
            x  = mod(a, n-1, n)
            if x != 1 :
                isPrime = False
                break
        if isPrime :
            break
    return n

