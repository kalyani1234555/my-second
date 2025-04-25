import timeit
text = "what have the romans ever done for us"


def comp_caps():

    captials = [char.upper() for char in text]
    # print(captials)
    return captials


# use map
def map_caps():
    map_capitals = list(map(str.upper, text))
    # print(map_capitals)
    return map_capitals


def comp_words():
    words = [word.upper() for word in text.split(" ")]
    # print(words)
    return words


def map_words():
    map_w = list(map(str.upper, text.split(" ")))
    # print(map_words)
    return map_w


# for x in map(str.upper, text.split(" ")):
#     print(x)


if __name__ == '__main__':
    print(comp_caps())
    print(map_caps())
    print(comp_words())
    print(map_words())
    # print(timeit.timeit("comp_caps()", setup="from map_intro import comp_caps", number=10000 ))
    print(timeit.timeit(comp_caps, number=100000))
    print(timeit.timeit(map_caps, number=100000))
    print(timeit.timeit(comp_words, number=100000))
    print(timeit.timeit(map_words, number=100000))
