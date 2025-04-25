number = "9,223;372:036 854,775;807"
seperators = number[1::4]
print(seperators)

result=""
# values ="".join(char if char not in seperators else " " for char in number).split()
for char in number:
    if char not in seperators:
        result += char
    else:
        result += " "
values = result.split()
print(result)
print(values)
