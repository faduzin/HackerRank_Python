import math

def find_theta(AB, BC) :
    print(round(math.degrees(math.atan2(AB,BC))),'\N{DEGREE SIGN}', sep='')

if __name__ == '__main__' :
    ab = int(input())
    bc = int(input())
    find_theta(ab, bc)