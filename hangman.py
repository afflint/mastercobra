
# -*- coding: utf-8 -*-
__project__ = 'mastercobra'
__author__ = 'Alfio Ferrara'
__email__ = 'alfio.ferrara@unimi.it'
__institution__ = 'Università degli Studi di Milano'
__date__ = '20 nov 2020'
__comment__ = '''
    Implementing the hangman game
    '''
from typing import List, Dict
import numpy as np


class Hangman(object):

    def __init__(self,
                 list_of_words: List[str],
                 word_len: int = 6,
                 trials: int = 8):
        self._idx = {}
        self.word_len, self.trials = word_len, trials
        self._update_index(list_of_words)
        self.selected_word = None
        self._select_word()
        self.mask = ['_'] * len(self.selected_word)

    def _update_index(self, list_of_words: List[str]):
        for word in list_of_words:
            try:
                self._idx[len(word)].append(word)
            except KeyError:
                self._idx[len(word)] = [word]

    def get_words(self, length: int):
        try:
            return self._idx[length]
        except KeyError:
            return []

    def add_words(self, list_of_words: List[str]):
        self._update_index(list_of_words)

    def print_status(self):
        print(self.mask)
        print('\nRemaining trials {}'.format(self.trials))

    def play(self, guess: str):
        self.trials -= 1
        for i, ch in enumerate(self.selected_word):
            if guess[i] == ch:
                self.mask[i] = ch

    def _select_word(self):
        try:
            candidates = self._idx[self.word_len]
            self.selected_word = np.random.choice(candidates)
        except KeyError:
            print(
                'Unavailable words of len {}'.format(
                    self.word_len))


class FreqHangman(Hangman):

    def __init__(self, list_of_words: List[str], freq: Dict[str, int],
                 word_len: int = 6, trials: int = 8):
        self.freq = freq
        self.N = sum(self.freq.values())
        super().__init__(list_of_words, word_len=word_len, trials=trials)

    def _select_word(self):
        try:
            candidates = self._idx[self.word_len]
            p = np.array([self.freq[x] for x in candidates])
            p = p / p.sum()
            self.selected_word = np.random.choice(candidates, p=p)
        except KeyError:
            print(
                'Unavailable words of len {}'.format(
                    self.word_len))

    def probability(self, word):
        try:
            return self.freq[word] / self.N
        except KeyError:
            return np.nan
