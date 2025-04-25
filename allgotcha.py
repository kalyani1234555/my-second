entries = []

# print("all: {}".format(all(entries)))
# print("any: {}".format(any(entries)))

if entries:
    print("all: {}".format(all(entries)))
else:
    print(False)
print("any: {}". format(any(entries)))

# result = bool(entries) and all(entries)
# result = entries and all(entries)
# result = all(entries)
result = any(entries)
print(result)
