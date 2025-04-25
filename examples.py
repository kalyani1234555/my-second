def factorial(n):
    # n! can also be defined as n * (n-1)!
    if n <= 1:
        return 1
    else:
        print(n / 0)
        return n * factorial(n-1)

try:
    print(factorial(900))
# except RecursionError:
#     print("This program calculate factorials that large")
# except ZeroDivisionError:
#     print("What are doing dividing by zero????")
except (RecursionError, OverflowError):
    print("This program cannot calculate factorials that large")
print("Program terminating")
