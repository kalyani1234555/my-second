import sys

# big_range = range(10000)
#
# print("big_range is {} bytes".format(sys.getsizeof(big_range)))
#
# # create a list containing all the values in big_range
# big_list = []
# for val in big_range:
#     big_list.append(val)
#
# print("big_range is {} bytes".format(sys.getsizeof(big_list)))


def my_range(n: int):
    print("my_range starts")
    start = 0
    while start < n:
        print("my_range is returning {}".format(start))
        yield start
        start += 1


big_range = range(5)
# _ = input("line 23")
# big_range = my_range(5)
# _ = input("line 25")

# print(next(big_range))
print("big_range is {} bytes".format(sys.getsizeof(big_range)))

# create a list containing all the values in big_range
big_list = []
# _ = input("line 31")
for val in big_range:
    # _ = input("line 33 - inside the loop")
    big_list.append(val)

print("big_range is {} bytes".format(sys.getsizeof(big_list)))

print(big_range)
print(big_list)

print("looping again .... or not")
# for i in big_range:
#     print("i is {}".format(i))

# for i in my_range(5):
#     print("i is {}".format(i))

for i in big_range:
    print("i is {}".format(i))
