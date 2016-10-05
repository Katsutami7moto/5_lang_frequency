import os
import re
import operator
import collections

QUANTITY_OF_RESULTS_TO_SHOW = 10


def load_data(filepath: str) -> str:
    if not os.path.exists(filepath):
        return None
    with open(filepath, encoding='utf-8') as handle:
        return handle.read()


def get_most_frequent_words(text: str) -> dict:
    all_words = re.findall(r'\w+', text.lower())
    words_counts = dict()
    for word in all_words:
        if word not in words_counts:
            words_counts[word] = all_words.count(word)
    result = sorted(words_counts.items(), key=operator.itemgetter(1), reverse=True)
    return result[:QUANTITY_OF_RESULTS_TO_SHOW]


if __name__ == '__main__':
    while True:
        path = input('Input a path to your .txt file: ')
        if not path:
            break
        data = load_data(path)
        if not data:
            print('File is empty or not a text.')
            break
        words_to_print = get_most_frequent_words(data)
        print("Most frequent words in {}:\n".format(path))
        [print('{}: {}'.format(key, str(value))) for key, value in words_to_print]
