#!/usr/bin/env python3

def return_evens(num_list):
    # pass
    # num_list = range(1,10,2)
    even= [n for n in num_list if n % 2 == 0]
    return even

def make_exclamation(sentence_list):
    # pass
    sentence = [sen + '!' for sen in sentence_list]
    print(sentence)
    return sentence