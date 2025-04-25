#                   1
#         012345678901234
parrot = "Norwegian Blue"

print(parrot[0:6])  # Norweg
print(parrot[3:5])  # we
print(parrot[0:9])  # Norwegian    
print(parrot[:9])   # Norwegian

print(parrot[10:14])  # Blue
print(parrot[:6])     # Norweg
print(parrot[6:])     # ian Blue
print(parrot[:])      # Norwegian Blue
print(parrot[:6] + parrot[6:])  # Norwegian Blue

print()
print(parrot[0:6])  # Norweg
print(parrot[-14:-8])
print(parrot[-9:7])

print(parrot[-14:])  # Norwegian Blue
print(parrot[:-14])  # no results
print(parrot[-4:-2])  # Bl
print(parrot[-4:12])   # Bl
print(parrot[-1:])
# slice with step
print(parrot[0:6:2])   # Nre
print(parrot[0:6:3])   # Nw
print(parrot[0:8:3])   # Nwi

number = '9,223,372,036,854,775,807'
print(number[1::4])  # ,,,,,,

number = '9,223;372,036,854,775;807'
print(number[1::4])  # ,;:,,;
print(number[-14::-2])  # 3:7;2,
print(number[-14:-4:-2])  # 3:7;


number = "9,223;372:036 854,775;807"
seperators = number[1::4]
print(seperators)

values ="".join(char if char not in seperators else " " for char in number).split()
# print([int(val) for val in values])
print(values)
