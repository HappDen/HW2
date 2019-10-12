a = int(input())
b = int(input())
a1 = int(input())
b1 = int(input())
if (a + b) < (a1 + b1) and a1 > b1 and a + 5 == a1 and b + 2 == b1:
   print("YESSSS!")
elif (a + b) < (a1 + b1) and a1 < b1 and a + 2 == a1 and b + 5 == b1:
    print("YESSSS!")
elif (a + b) > (a1 + b1) and a < b and a - 2 == a1 and b - 5 == b1:
    print("YESSSS!")
elif (a + b) > (a1 + b1) and a > b and a - 5 == a1 and b - 2 == b1:
    print("YESSSS!")
else:
    print ("No no")
