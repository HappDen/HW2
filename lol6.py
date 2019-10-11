import math
a = int(input())
b = 0
domag2 = 0
domag1 = 0
while b < a:
    domag1 = int(input("celoe "))
    domag2 += domag1/int(input("dr "))
    print(domag2)
    b = b + 1

print(domag2,"/100")

