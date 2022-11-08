# x3 = m^2 - x1 - x2 mod p
#y3 = m(x1 - x3) - x1 mod p

#add two points on an elliptic curve

#two different points
def sum (b, c, p, x1, y1, x2, y2):
    if (x1 == x2) and (y1 == y2):
        m = ((3*x1*x1) + b) / (2*y1)
    else:
        m = (y2 - y1) / (x2 - x1)

    if m%1 != 0:
        for i in range (0, p):
            if (3*i)%p == 1:
                m = i
                break
    m = m%p
    x3 = m**2 - x1 - x2
    x3 = x3 % p
    y3 = (m*(x1 - x3)) - y1
    y3 = y3%p
    print(x3)
    print(y3)
    return x3, y3

#same point, finding 2P
def sum2P(b, c, p, x, y):
    RHS = (3*x*x + b)
    LHS = (2*y)
    implicitDeriv =  RHS/ LHS
    print(implicitDeriv)
    if (implicitDeriv%1 != 0):
        multiplier = 1
        for i in range(0, p):
            if (i*LHS)%p == 1:
                multiplier = i
                print(multiplier)
                break
    implicitDeriv = (3*x*x + b) * multiplier
    implicitDeriv = implicitDeriv%p

    x3 = implicitDeriv*implicitDeriv - x - x
    y3 = implicitDeriv*(x-x3) - y
    x3 = x3 % p
    y3 = y3 % p
    print(x3, y3)
    



def main():
    #examples
    print(sum(4, 4, 2773, 1, 3, 1, 3))
    sum2P(4, 4, 2773, 1, 3)


main()
