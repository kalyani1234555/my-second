for i in range(1, 13):
    print("The no.{0} squares {1} cubes {2}".format(i, i ** 2, i ** 3))
print()
for i in range(1, 13):
    print("The no.{0:2} squares {1:3} cubes {2:4}".format(i, i ** 2, i ** 3))
print()
for i in range(1, 13):
    print("The no.{0:2} squares {1:<3} cubes {2:^4}".format(i, i ** 2, i ** 3))

print()
print("Pi is approximately {0:12}".format(22/7))
print("Pi is approximately {0:12f}".format(22/7))
print("Pi is approximately {0:12.50f}".format(22/7))
print("Pi is approximately {0:52.50f}".format(22/7))
print("Pi is approximately {0:62.50f}".format(22/7))
print("Pi is approximately {0:<72.50f}".format(22/7))
print("Pi is approximately {0:<72.54f}".format(22/7))

print()
for i in range(1, 13):
    print("The no.{} squares {} cubes {}".format(i, i ** 2, i ** 3))

print()
for i in range(1, 13):
    print("The no.{} squares {} cubes {:4}".format(i, i ** 2, i ** 3))
