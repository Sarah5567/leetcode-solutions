class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        shortest_path = {word : 0 for word in wordList}
        shortest_path[beginWord] = 1

        if not endWord in wordList:
            return 0

        continuation_words = defaultdict(list)
        for word in wordList:
            begin = ""
            for i, ch in enumerate(word):
               continuation_words[begin + '_' + word[i + 1:]].append(word)
               begin += ch


        q = deque()
        q.append(beginWord)

        while q and not shortest_path[endWord]:
            word = q.popleft()
            begin = ""

            for i, ch in enumerate(word):
                pattern = begin + '_' + word[i + 1:]
                for continuation_word in continuation_words[pattern]:

                    if not shortest_path[continuation_word]:
                        shortest_path[continuation_word] =  shortest_path[word] + 1
                        q.append(continuation_word)

                begin += ch

        return shortest_path[endWord]
