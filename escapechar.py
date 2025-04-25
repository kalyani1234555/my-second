# The backslash character has got a special meaning in strings.It's used to escape the character that follows it,
# to give that character special meaning. ex:\n to start a new line, \t to insert a tab.

split_string = "This string has been\nsplit over\nseveral\nlines"
print(split_string)  # whenever the print f'n sees backslash n in string, it causes it to start a new line.

# backslash t causes python to tab to the next stop before printing.
tappedString = "1\t2\t3\t4\t5"
# tappedString = "1 2 3 4 5"
print(tappedString)

# backslash can also be used to escape special characters, such as quotes and double quotes, and that can be useful
# if you've got a string containing both of those characters.
print('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting".')
# or
print("The pet shop owner said \"No, no, 'e's uh,...he's resting\".")
# basically, when we're using triple quotes there, there's no need to escape any quotes inside the string.
# python feature provides three consecutive quotes because to make strings spanning lines more readable.
print("""The pet shop owner said "NO, no, 'e's uh,...he's resting". """)
print("""The pet shop owner said "NO, no, \
'e's uh,...he's resting". """)

# string that we split over several lines earlier, is not easy to read because of the embedded backslash ns. but python
# allows the string to be spilt over several lines without doing that, by using triple quotes.

another_spilt_string = """This string has been 
splitover 
several 
lines """

print(another_spilt_string)

# every one to start with new line when printed, then what you can do is escape the end of a line with a backslash.
another_spilt_string1 = """This string has been \
splitover \
several \
lines """

print(another_spilt_string1)

# include the backslash character in your string

print("c:\\users\\timbuchalka\\notes.txt")  # we told python that we want the backslash character to be output.
print(r"c:\users\timbuchalka\notes.txt")  # second way to use a raw string. Raw string intended for use with regular
# expressions, and we can create a raw string by prefixing the string with the letter r, r for raw.

# note: in general, recommend using the first method, escaping your backslash characters.
