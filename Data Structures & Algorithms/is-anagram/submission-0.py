class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        freqS = Counter(s)
        freqT = Counter(t)
        if len(freqS) != len(freqT):
            return False

        for char , count in freqS.items():
            if freqT.get(char) != count:
                return False
        return True