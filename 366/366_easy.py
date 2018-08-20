#!/usr/bin/env python3

import sys

def find_words(big_word, dictionary):
    possible_words = set([big_word[0:i]+big_word[i+1:] for i in range(len(big_word))])
    return [word for word in possible_words if (word in dictionary)]

def largest_words(dictionary):
    my_dict = {}
    for word in dictionary:
        my_dict[word] = find_words(word, dictionary)
    max_len = len(max(my_dict.values(), key=lambda x: len(x)))
    return [(key, val) for key,val in my_dict.items() if len(val) == max_len]

if __name__=='__main__':
    words = sys.stdin.readlines()
    words = set([word.strip() for word in words])
    for largest in largest_words(words):
        print('{}: {}'.format(largest[0], largest[1]))
