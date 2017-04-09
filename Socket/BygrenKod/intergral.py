a = float(input("Lower bound: "))
b = float(input("Higher bound: "))

n = 10000
area = 0

delta = (b - a)/n
x = a + delta/2

while x < b:
    y = x**2
    area += delta*y
    x += delta

print("I = " + str(area))