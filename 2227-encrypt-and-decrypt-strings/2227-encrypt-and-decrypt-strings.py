class Encrypter:

    def __init__(self, keys, values, dictionary):
        self.keys_map = {k: v for k, v in zip(keys, values)}
        self.dictionary = dictionary
        self.encrypt_cache = {}

    def encrypt(self, word1: str) -> str:
        if word1 in self.encrypt_cache:
            return self.encrypt_cache[word1]

        res = []
        for ch in word1:
            if ch not in self.keys_map:
                return ""
            res.append(self.keys_map[ch])
        joined_res = "".join(res)

        if word1 in self.encrypt_cache:
            self.encrypt_cache[word1] = joined_res
        return joined_res

    def decrypt(self, word2: str) -> int:
        count = 0
        for word in self.dictionary:
            if self.encrypt(word) == word2:
                count += 1
        return count
