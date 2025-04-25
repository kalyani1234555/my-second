def banner_text(text: str = " ", screen_width: int = 80) -> None:
    """ print a string centred, with ** either side.
    :param text: The string to print
        An asterisk(*) will result in a row of asterisk.
        The default will print a blank line,with a ** boarder at
        the left and right edges
    :param screen_width: The overall width to print within
        (including the 4 spaces for the ** either side)
    : raise ValueError: if the supplied string is too long to fit.
    """
    # screen_width = 50
    if len(text) > (screen_width - 4):
        # print("EEK!!")
        # print("THE TEXT IS TOO LONG TO FIT IN THE SPECIFIED WIDTH")
        raise ValueError("String {0} is larger then specified width {1}"
                         .format(text, screen_width))

    if text == "*":
        print("*" * screen_width)
        # print(screen_width)
    else:
        # center_text = text.center(screen_width - 4)
        # print("**{0}**".format(center_text))
        # print("**{0}**".format(text.center(screen_width - 4)))
        output_string = ("**{0}**".format(text.center(screen_width - 4)))
        print(output_string)


help(banner_text)
banner_text("*", 60)
banner_text("Always look on the bright side of life...", 60)
banner_text("If life seems jolly rotten", 60)
banner_text("There's something you've forgotten!", 60)
banner_text("And that's to laugh and smile and dance and sing,", 60)
banner_text(screen_width=60)
banner_text("When you're feeling in the dumps,", 60)
banner_text("Don't be silly chumps", 60)
banner_text("*", 60)

# result = banner_text("Nothing is returned")
# print(result)
#
# numbers = [4, 2, 7, 5, 8, 3, 9, 6, 1]
# print(numbers.sort())
