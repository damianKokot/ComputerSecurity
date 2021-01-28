def count():
    dictionary = {}
    total = 0
    with open("slownik") as slownik:
        for char in slownik.read():
            total += 1
            if char not in dictionary.keys():
                dictionary[char] = 1
            else:
                dictionary[char] = dictionary.get(char) + 1

    for char, value in dictionary.items():
        print(char, ":", value, "/",  total)


count()