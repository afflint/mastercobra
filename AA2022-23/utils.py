from collections import defaultdict


def change_char(name, new_char, wrong_char_pos=0):
    new_name = name[:wrong_char_pos] + new_char + \
               name[wrong_char_pos+1:]
    return new_name, name


class CharIndex(object):
    """
    Structure of the class
    - variables: history, index {char: count}
    - methods: read_text, clean_text, update_index
    """
    def __init__(self, min_char=0):
        self.history = []
        self.index = defaultdict(lambda: 0)
        self.min_char = min_char

    def read_text(self, filename):
        with open(filename, 'r') as infile:
            text = infile.readlines()
        clean_text = self.clean_text(text)
        return clean_text

    def clean_text(self, list_of_str):
        return [x.strip() for x in list_of_str if
                len(x.strip()) > self.min_char]

    def update_index(self, clean_text):
        for s in " ".join(clean_text):
            self.index[s] += 1

    def index_text(self, filename):
        self.history.append(filename)
        clean_text = self.read_text(filename)
        self.update_index(clean_text)

    def size(self):
        return sum(self.index.values())

    def vocabulary(self):
        return list(self.index.keys())

    def p(self, char):
        return self.index[char] / self.size()
