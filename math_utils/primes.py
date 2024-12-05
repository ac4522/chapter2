from math import sqrt


def isprime(a):
    if a == 1:
        return False
    elif a==2 or a==3:
        return True
    for i in range(2, int(sqrt(a)+1)):
        if a % i == 0:
            return False
    return True
