class Encrypter:

    def __init__(self, keys, values, dictionary):
        self.keys_map = {k: v for k, v in zip(keys, values)}
        self.encrypted_dictionary = defaultdict(int)

        for word in dictionary:
            encrypted = self.encrypt(word)
            self.encrypted_dictionary[encrypted] += 1

    def encrypt(self, word1: str) -> str:
        res = []
        for ch in word1:
            if ch not in self.keys_map:
                return ""
            res.append(self.keys_map[ch])
        return "".join(res)

    def decrypt(self, word2: str) -> int:
        return self.encrypted_dictionary[word2]
