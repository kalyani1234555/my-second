entries = [1, 2, 3, 4, 5]

print("all: {}".format(all(entries)))
print("any: {}".format(any(entries)))

print("Iterable with a 'False' value")
entries_with_zero = [1, 2, 0, 4, 5]

print("all: {}".format(all(entries_with_zero)))
print("any: {}".format(any(entries_with_zero)))

print()
print("values interpreted as False in Python")
print("""False: {0}
None: {1}
0: {2}
0.0: {3}
empty list []: {4}
empty tuple (): {5}
empty string '' : {6}
empty string "": {7}
empty mapping {{}}: {8}
""".format(False, bool(None), bool(0), bool(0.0), bool([]), bool(()), bool(''), bool(""), bool({})))

print("=" * 80)
name = "Tim"
if name:
    print("Hello {}".format(name))
else:
    print("Welcome, person with no name")


# # Check if any value is greater than 10
# numbers = [2, 7, 12, 9]
# result_any = any(x > 10 for x in numbers)  # True because 12 is greater than 10
# print(result_any)
#
# # Check if all values are greater than 3
# result_all = all(x > 3 for x in numbers)  # False because 5, 7, 12, 9 are > 3, but 5 isn't
# print(result_all)
