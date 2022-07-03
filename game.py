import random

WORD_CORRECT = 2
WORD_WRONT_SPOT = 1
WORD_NO = 0

class WordleGame:
    wordlib = []

    def __init__(self, ko, wordlib) -> None:
        self.ko = ko
        self.wordlib = wordlib


    def guessWord(self, word: str, wordle: str = ""):
        word = word.lower()
        assert(len(word) == 5)
        assert(word in self.wordlib)
        if wordle == "":
            wordle = random.choice(self.ko)
        scores = [0] * 5
        for i in range(5):
            if word[i] == wordle[i]:
                scores[i] = WORD_CORRECT
            elif word[i] in wordle:
                scores[i] = WORD_WRONT_SPOT
            else:
                scores[i] = WORD_NO
        return scores

    def findNext(self, word, scores, wordlist):
        filter_list = wordlist.copy()
        for i in range(5):
            if scores[i] == WORD_NO:
                # Not include
                filter_list = [x for x in filter_list if word[i] not in x]
            elif scores[i] == WORD_WRONT_SPOT:
                filter_list = [x for x in filter_list if word[i] in x and word[i] != x[i]]
            elif scores[i] == WORD_CORRECT:
                filter_list = [x for x in filter_list if word[i] == x[i]]
        return filter_list
    

    def findBestGuess(self, wordlist, allowDup=False):
        all_scores = []

        for guess in wordlist:
            total_score = 0
            dupFactor = 1
            if not allowDup and len(set(guess)) != len(guess):
                dupFactor = 10
            for wordle in wordlist:
                score = self.guessWord(guess, wordle)
                total_score += (sum(score)/10)**10
            total_score = total_score / len(wordlist)
            all_scores.append(total_score / dupFactor)

        s_scores, s_wordlist = (list(x) for x in zip(*sorted(zip(all_scores, wordlist), key=lambda pair: pair[0])))
        return s_scores, s_wordlist
