class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = [0] * 26
        for ch in word:
            freq[ord(ch) - ord('a')] += 1

        freq.sort()

        left = 0
        while left < 26 and not freq[left]:
            left += 1

        right = left
        cur_length = 0
        best = float('inf')

        while left < 26:
            while right < 26 and freq[right] - freq[left] <= k:
                cur_length += freq[right]
                right += 1

            total_length = cur_length + (26 - right) * (freq[left] + k)

            best = min(best, len(word) - total_length)

            cur_length -= freq[left]
            left += 1
            
        return best if best != float('inf') else 0