n, d = 0, 1
for i in range(int(input())):
    a, b = int(input()), int(input())
    n = n * b + a * d
    d *= b
x, y = n, d
while y > 0:
    x, y = y, x % y
print(n // x, '/', d // x, sep='')
