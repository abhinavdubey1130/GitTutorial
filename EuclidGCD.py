## Euclid's Algorithm
## Author : Abhinav Dubey
## Date   : Jun 19, 2022


def Euclid(x, y):
    ''' Takes two integers as input and
        returns greatest common divisor.'''

    x = abs(x); y = abs(y)
    if x == 0 or y == 0:
        return ("Error , number can't be zero !")
    
    if x == y:
        return x
    elif x < y:
        y = y - x
        d = Euclid(x, y)
    elif x > y:
        x = x - y
        d = Euclid(x, y)

    return d

# Test cases
print(Euclid(3, 7))
print(Euclid(12,8))
print(Euclid(0,12))
print(Euclid(23, -46))


