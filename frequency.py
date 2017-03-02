""" Analyzes the word frequencies in a book downloaded from
Project Gutenberg """

import string


def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """
    f = open(file_name, 'r')
    lines = f.readlines()
    curr_line = 0
    while lines[curr_line].find('Actus primus') == -1:
        curr_line += 1
    lines = lines[curr_line+1:]
    words = []
    for line in lines:
        line = line.translate(line.maketrans('', '', string.punctuation))
        line = line.lower()
        line = line.strip()
        words += line.split()
    return words


def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequentlyoccurring
    """
    commonest_words = []
    wordfreq = [word_list.count(p) for p in word_list]
    word_counts = dict(zip(word_list, wordfreq))
    ordered_by_frequency = sorted(word_counts, key=word_counts.get,
                                  reverse=True)
    for i, word in enumerate(ordered_by_frequency):
        commonest_words.append(word)
        if i > n:
            return commonest_words


if __name__ == "__main__":
    print("Running WordFrequency Toolbox")
    print(get_top_n_words(get_word_list('shakespeare.txt'), 100))
