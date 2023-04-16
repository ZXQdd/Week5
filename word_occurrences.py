WORD_COUNT = {}

input_str = input("Please enter a string: ")
for word in input_str.split():
    if word in WORD_COUNT:
        WORD_COUNT[word] += 1
    else:
        WORD_COUNT[word] = 1
for key, value in sorted(WORD_COUNT.items()):
    print("{:{}} {}".format(key + ":", 11, value))