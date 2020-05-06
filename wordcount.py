import sys

def count_word_occurences(path):

    text_file = open(path)

    word_count_dict = {}

    for line in text_file:
        line = line.rstrip()
        words = line.split()

        for word in words:
            word = word if word.isalnum() else world[:-1]
            word_count_dict[word] = word_count_dict.get(word,0) + 1

    for word, count in word_count_dict.items():
        print(word, count)

def tokenize(path):

    text_file = open(path)

    tokens = []

    for line in text_file:
        line = line.rstrip()
        words = line.split()

        for word in words:
            word = word.strip("'\",.!?-#$%^&();:_")
            word = word.lower()
            tokens.append(word)

    return tokens

def count_tokens(tokens):
    """Return dictionary with word as key and word count as value"""

    word_dict = {}

    for word in tokens:
        word_dict[word] = word_dict.get(word,0) + 1

    return word_dict

def print_word_count(word_count_dict):
    
    for word, count in word_count_dict.items():
        print(word, count)

print(tokenize("test.txt"))

# print_word_count(count_tokens(tokenize("twain.txt")))








