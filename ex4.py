"""
Given an input string, count occurrences of all characters within a string (e.g. pythonnohtyppy -> p:3, y:3, t:2, h:2, o:2, n:2)
"""

import argparse

try:
    parser = argparse.ArgumentParser(description="Read a word and gives the count of every letter")
    parser.add_argument('-word', help='read the word')
    args = parser.parse_args()

    word = args.word

    if len(word) == 0: raise Exception("NoWordProvided")
    letter_count={}

    for letter in word:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    print(f'The counts of every letter in word "{word}" are:\n', letter_count)
except Exception as err:
    print(err.args[0])