'''
This simple code generates n GCD numbers 
with k steps to find them via Euclidean algorithm.

Educational purposes only. Just to create some examples for students to practice
Euclidean Method.

by Mateusz Demon (MatDemn: https://github.com/MatDemn)
'''

# How many tries does the scrpt have to take to find random numbers.
# Increase this value if you're losing hope of finding some examples.
# But you know, for your own risk. Your computer may fly into the oblivion
# if this value is too high.
MAX_NUMBER_OF_TRIES = 100

# Range in which the algorithm will search for example numbers.
LOWER_BOUND = 100
UPPER_BOUND = 1000

# How many examples you'd like to see
N = 3

# How many steps at least does it have to take to find this GCD.
K = 10

import random

def gcd_gen(n: int, k: int):
    result = []

    def NWD_MODULO(a, b):
        k = 0
        while(b>0):
            t = b
            b = a % b
            a = t
            k+=1
        return (a, k)
    
    killSwitch = MAX_NUMBER_OF_TRIES
    while(n > 0):
        a = random.randint(LOWER_BOUND, UPPER_BOUND)
        b = random.randint(LOWER_BOUND, UPPER_BOUND)

        while((nwd_res := NWD_MODULO(a,b))[1] < k and killSwitch > 0):
            a = random.randint(LOWER_BOUND, UPPER_BOUND)
            b = random.randint(LOWER_BOUND, UPPER_BOUND)
            killSwitch-=1

        if(killSwitch == 0):
            return []
        
        killSwitch = MAX_NUMBER_OF_TRIES

        result.append((a,b,nwd_res))
        n-=1
    return result

print(gcd_gen(N, K))
    
    
    