class Solution:
    def fill_words_parts(self, words_parts: Dict[str, List[int]], wordList: List[str]) -> None:
        for word_index, word in enumerate(wordList):
            for i in range(len(word)):
                part = word[:i] + word[i + 1:]
                words_parts[part].append(word_index)

    def differ_by_one(self, w1: str, w2: str) -> bool:
        diff = 0
        for a, b in zip(w1, w2):
            if a != b:
                diff += 1
                if diff > 1:
                    return False
        return diff == 1

    def bfs(
        self,
        wordList: List[str],
        words_parts: Dict[str, List[int]],
        begin_index: int,
        end_index: int
    ):
        n = len(wordList)
        dist = [-1] * n
        parents = defaultdict(list)

        queue = deque([begin_index])
        dist[begin_index] = 0
        found_end = False

        while queue and not found_end:
            level_size = len(queue)

            for _ in range(level_size):
                index = queue.popleft()
                word = wordList[index]

                for i in range(len(word)):
                    part = word[:i] + word[i + 1:]
                    for next_word in words_parts[part]:
                        if not self.differ_by_one(word, wordList[next_word]):
                            continue

                        if dist[next_word] == -1:
                            dist[next_word] = dist[index] + 1
                            parents[next_word].append(index)
                            queue.append(next_word)

                            if next_word == end_index:
                                found_end = True

                        elif dist[next_word] == dist[index] + 1:
                            if index not in parents[next_word]:
                                parents[next_word].append(index)

        return dist, parents

    def build_paths(
        self,
        index: int,
        begin_index: int,
        parents: Dict[int, List[int]],
        wordList: List[str],
        path: List[str],
        res: List[List[str]]
    ):
        if index == begin_index:
            res.append(path[::-1])
            return

        for p in parents[index]:
            self.build_paths(
                p,
                begin_index,
                parents,
                wordList,
                path + [wordList[p]],
                res
            )

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []

        wordList = wordList + [beginWord]
        begin_index = len(wordList) - 1
        end_index = wordList.index(endWord)

        words_parts = defaultdict(list)
        self.fill_words_parts(words_parts, wordList)

        dist, parents = self.bfs(wordList, words_parts, begin_index, end_index)

        if dist[end_index] == -1:
            return []

        res = []
        self.build_paths(
            end_index,
            begin_index,
            parents,
            wordList,
            [wordList[end_index]],
            res
        )

        return res
