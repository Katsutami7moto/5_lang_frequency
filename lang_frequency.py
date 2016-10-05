import os
import re
from collections import Counter

QUANTITY_OF_RESULTS_TO_SHOW = 10


def load_data(filepath: str) -> str:
    if not os.path.exists(filepath):
        return None
    with open(filepath, encoding='utf-8') as handle:
        return handle.read().lower()


def get_most_frequent_words(text: str) -> dict:
    all_words = re.findall(r'\w+', text)
    return Counter(all_words).most_common(QUANTITY_OF_RESULTS_TO_SHOW)


if __name__ == '__main__':
    while True:
        path = input('Input a path to your .txt file: ')
        if not path:
            break
        data = load_data(path)
        if not data:
            print('File is empty or not a text.\n')
            break
        words_to_print = get_most_frequent_words(data)
        print('\nMost frequent words in "{}":\n'.format(path))
        [print('{}: {}'.format(*word)) for word in words_to_print]
        print()
