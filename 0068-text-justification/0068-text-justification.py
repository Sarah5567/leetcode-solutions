class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        answer = []
        cur_words = []
        cur_length = 0

        for word in words:
            if cur_length + len(word) + (1 if cur_words else 0) <= maxWidth:
                cur_length += len(word) + (1 if cur_words else 0)
                cur_words.append(word)
            else:
                line = cur_words[0]
                if len(cur_words) > 1:
                    spaces = (maxWidth - cur_length) // (len(cur_words) - 1)
                    extra_spaces = (maxWidth - cur_length) % (len(cur_words) - 1)

                    for i in range(1, len(cur_words)):
                        line += ' ' * (spaces + 1)
                        if i <= extra_spaces:
                            line += ' '
                        line += cur_words[i]
                else:
                    line += ' ' * (maxWidth - len(line))
                    
                answer.append(line)

                cur_words = [word]
                cur_length = len(word)

        last_line = ' '.join(cur_words)
        last_line += ' ' * (maxWidth - cur_length)
        answer.append(last_line)

        return answer
