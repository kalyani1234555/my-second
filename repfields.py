age = 24
print("My age is " + str(age) + "  years")

print()
print("My age is {0} years".format(age))
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
      .format(31, " jan", "mar", "may", "jul", "aug", "oct", "dec"))
print("There are {0} days in jan, mar, may, jul, aug, oct and dec".format(31))
print("There are jan: {2}, feb : {0}, mar : {1}, apr : {2}, may : {1}, aug : {2}, oct : {1} and dec : {2}"
      .format(28, 30, 31))
print("""There are jan: {2}
feb : {0} 
mar : {1} 
apr : {2} 
may : {1} 
aug : {2} 
oct : {1} and 
dec : {2} 
""".format(28, 30, 31))
