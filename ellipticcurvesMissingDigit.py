
#  y^2 = x^3 + 7x + 11 mod 593899
# x = 12345_
#looking for the missing last digit of the x coordinate above that makes (x, y) a point on the curve
import math
def getYsquared(x):
    ySquared = (x*x*x) + (2*x) + 3
    return ySquared

def isPerfectSquare(ySquared):
    if (int(math.sqrt(ySquared)+.5)**2) == ySquared:
        return True
    return False

def check(x, y,p):
   rightHandSide = x**3 + 7*x + 11
   leftHandSide = y**2
   print("RHS: ", rightHandSide, "LHS: ", leftHandSide)
   print("RHS%p: ", rightHandSide%p)
   print("LHS%p: ", leftHandSide%p)

def getYsquaredTest(x, p):
    ySquared = (x*x*x) + (7*x) + 11
    # y2 = 4

    if ySquared%p == 0:
        print("y=0")

    perfSquare = isPerfectSquare(ySquared)
    allDown = False
    while (perfSquare == False):
        if allDown:
            ySquared = ySquared + p
            if (isPerfectSquare(ySquared)):
                perfSquare = True

        elif (ySquared == ySquared%p):
            if (isPerfectSquare(ySquared)):
                perfSquare = True
            else:
                allDown = True
        else:
            ySquared = ySquared%p
    print("x = ", x, "y= ", math.sqrt(ySquared))
    check(x, math.sqrt(ySquared), p)

def main():



    num = 123450

    #123450 and 123451 took too long
    for i in range(2, 10):
        num += i
        getYsquaredTest(num, 593899)
        num -=i


main()


'''
points on curve y2 = x^3 + 7x + 11 mod 593899: (123452, 55886), (123453, 65243), (123454, 26651) 
'''