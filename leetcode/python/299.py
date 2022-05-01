from collections import defaultdict
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        hash = defaultdict(int)
        for c in secret: hash[c] += 1
        tot = 0
        for c in guess:
            if hash[c]:
                tot += 1
                hash[c] -= 1

        bulls = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1

        return str(bulls) + 'A' + str(tot - bulls) + 'B'
