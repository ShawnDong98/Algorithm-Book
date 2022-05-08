class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        while i < len(words):
            j = i + 1
            l = len(words[i])
            while j < len(words) and l + 1 + len(words[j]) <= maxWidth:
                l += 1 + len(words[j])
                j += 1

            line = ''
            if (j == len(words) or j == i + 1):
                line += words[i]
                for k in range(i + 1, j): line += ' ' + words[k]
                while len(line) < maxWidth: line += ' '
            else:
                cnt = j - i - 1
                r = maxWidth - l + cnt
                line += words[i]
                k = 0
                while k < r % cnt:
                    line += (r//cnt+1) * ' ' + words[i + k + 1]
                    k += 1
                while k < cnt:
                    line += r//cnt * ' ' + words[i + k + 1]
                    k += 1

            res.append(line)
            i = j - 1
            i += 1
        return res
