# binding couple of labels to two int values
a = 12
b = 3

print(a+b)     # 15
print(a - b)   # 9
print(a * b)   # 36  (x is a valid name for a variable, which means we have to use the * for multiplication)
print(a / b)   # 4.0
print(a // b)  # 4 integer division, rounded down towards minus infinity
print(a % b)   # 0 modulo: the remainder after integer division

print()

# for i in range(1, 4):
#     print(i)

# for i in range(1, a/b):
#      print(i)  # we will get the TypeError

for i in range(1, a//b):
    print(i)  # now      it works

print(a + b / 3 - 4 * 12)
print(a + (b / 3) - (4*12))
print((((a + b) /3) - 4) * 12)
print(((a + b) / 3 - 4) * 12)

c = a + b
d = c / 3
e = d - 4
print(e * 12)

print()

print(a / (b * a) / b)
