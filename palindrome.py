def is_palindrome(string: str) -> bool:                  # palindrome
    # backwards == string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


# word = input("please enter a word to check: ")
# if is_palindrome(word):
#     print("'{}' is a palindrome".format(word))
# else:
#     print("'{}' is not a palindrome".format(word))


def palindrome_sentence(sentence: str) -> bool:  # using the sentences
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)  # first part of function
    # return string[::-1].casefold() == string.casefold()
    return is_palindrome(string)   # calling the function from other function


word = input("please enter a word to check: ")
if palindrome_sentence(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))


p = palindrome_sentence()
