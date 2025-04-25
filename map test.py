text = "what have the romans ever done for us"

map_w = list(map(str.upper, text.split(" ")))
print(map_w)


def greet(name):
    return f"Hello,{name}!"


# calling function
greeting = greet("Alice")
print(greeting)


# Reference to the function
def say_hello(fun, name):
    print(fun(name))


say_hello(greet, "BOb")
