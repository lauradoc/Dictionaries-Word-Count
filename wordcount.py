
import sys

from collections import counter

text = sys.argv[1]



def word_count(text):
"""Returns number of times a word appears in text"""

    open_text = open(text)
    word_count = {}  
    all_words = []  

    for line in open_text:
        line = line.split(' ')
        punctuations = [',', '?', '.', '"', "'", ':']
        for word in line:
            for character in word:
                if character in punctuations:
                    word = word.replace(character, '')
            word = word.lower().strip()
            all_words.append(word)
            word_count[word] = word_count.get(word, 0) + 1

    for key, value in word_count.items():
            print(f'{key} {value}')

    return word_count

word_count(text)


def word_count_with_counter(text):

    open_text = text.read()
    text_without_punctuation = 

    #split into words

    c = Counter(f_cleaned)



