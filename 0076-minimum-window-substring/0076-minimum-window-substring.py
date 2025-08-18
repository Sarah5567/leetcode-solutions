class Solution:
    def amountPerLetter(self, t: str) -> Dict[str, int]:
        amountsDict = {}
        for c in t:
            if not c in amountsDict:
                amountsDict[c] = 1
            else:
                amountsDict[c] += 1
        return amountsDict

    def minWindow(self, s: str, t: str) -> str:
        currentAmounts = {c : 0 for c in t}
        requiredAmount = self.amountPerLetter(t)

        ans = ""
        begin, end, letterIncluded = 0, -1, 0

        while end < len(s):
            if letterIncluded < len(t):
                end += 1
                if end < len(s) and s[end] in requiredAmount:
                    currentAmounts[s[end]] += 1
                    if currentAmounts[s[end]] <= requiredAmount[s[end]]:
                        letterIncluded += 1
            else:
                if end - begin + 1 < len(ans) or ans == "":
                    ans = s[begin:end + 1]
                if s[begin] in requiredAmount:
                    currentAmounts[s[begin]] -= 1
                    if currentAmounts[s[begin]] < requiredAmount[s[begin]]:
                        letterIncluded -= 1 
                begin += 1

        return ans
                        