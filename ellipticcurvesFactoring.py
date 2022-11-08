# n = pq
import random
def sum(b, c, p, x1, y1, x2, y2):
    if (x1 == x2) and (y1 == y2):
        m = ((3 * x1 * x1) + b) / (2 * y1)
    else:
        m = (y2 - y1) / (x2 - x1)

    if m % 1 != 0:
        for i in range(0, p):
            if (3 * i) % p == 1:
                m = i
                break
    m = m % p
    x3 = m ** 2 - x1 - x2
    x3 = x3 % p
    y3 = (m * (x1 - x3)) - y1
    y3 = y3 % p

    return x3, y3


def sum2P(b, c, p, x, y):
    RHS = (3 * x * x + b)
    LHS = (2 * y)
    implicitDeriv = RHS / LHS
    if (implicitDeriv % 1 != 0):
        multiplier = 1
        for i in range(0, p):
            if (i * LHS) % p == 1:
                multiplier = i
                break
    implicitDeriv = (3 * x * x + b) * multiplier
    implicitDeriv = implicitDeriv % p

    x3 = implicitDeriv * implicitDeriv - x - x
    y3 = implicitDeriv * (x - x3) - y
    x3 = x3 % p
    y3 = y3 % p
    return (x3, y3)

def gcd(a, b):
    u = 1
    g = a
    x = 0
    y = b
    while(y!=0):
        if y == 0:
            v = (g-(a*u))/b
            return g, u, v
        else:
            t = g % y
            q = (g-t)/y
            t = g%y
            s =  u-q*x
            u = x
            g = y
            x = s
            y = t
            if y ==0:
                v = (g-a*u)/b
                return g
def getRandomInfo(n):
    #gives you random x and y coordinates within domain/range of elliptic curve, given that it is modulo n
    x = random.randint(1, 9)
    y = random.randint(1, 9)
    b = 4
    c = y**2 - x**3 - b*x
    return x, y, b, c

def main():
    #in theory you could use this, but we are actually gonna factor 2773
    #n = input("Enter the number you would like to factor (n): ")
    n = 2773
    #you could use line below, but for specific problem, we already know the point and function
    #x, y, b, c = getRandomInfo(n)
    x, y, b = 1, 3, 4
    c = y**2 - x**3 - b*x

    x2P, y2P = sum2P(b, c, n, 1, 3)
    deltaX = x2P - x
    deltaY = y2P - y
    factor = (gcd(deltaX, n))
    print(factor, n/factor)


main()