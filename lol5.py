x = int(input())
count = 0
for i in range (1,x + 1):
    if x % i == 0:
        count += 1
        print(i,end = " ")
if count == 2 :
    print(" ")
    print("AHTUNG")


