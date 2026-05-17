class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        secret_digits = [0] * 10
        guess_digits = [0] * 10

        for ch_secert, ch_guess in zip(secret, guess):
            if ch_secert == ch_guess:
                bulls += 1
            else:
                secret_digits[int(ch_secert)] += 1
                guess_digits[int(ch_guess)] += 1

        cows = 0
        for secret_count, guess_count in zip(secret_digits, guess_digits):
            cows += min(secret_count, guess_count)

        return f'{bulls}A{cows}B'
        