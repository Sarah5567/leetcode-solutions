class WordFilter:

    def __init__(self, words: List[str]):
        self.words = words
        self.words_dict = defaultdict(list)
        for idx, word in enumerate(words):
            for i in range(1, len(word) + 1):
                self.words_dict[word[:i]].append(idx)

        for words_list in self.words_dict.values():
            words_list.sort(reverse=True)

    def f(self, pref: str, suff: str) -> int:
        for idx in self.words_dict[pref]:
            if self.words[idx].endswith(suff):
                return idx
        return -1
