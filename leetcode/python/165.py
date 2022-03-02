class Solution:
    def compareVersion_v20220302(self, version1: str, version2: str) -> int:
        v1 = map(int, version1.split('.'))
        v2 = map(int, version2.split('.'))
        for i in range(max(len(v1), len(v2))):
            a = v1[i] if i < len(v1) else 0
            b = v2[i] if i < len(v2) else 0
            if a > b:
                return 1
            elif a < b:
                return -1
        return 0
    def compareVersion(self, version1: str, version2: str) -> int:
        i, j = 0, 0
        n1, n2 = len(version1), len(version2)
        while i < n1 or j < n2:
            v1, v2 = 0, 0
            while i < n1 and version1[i] != '.':
                v1 = v1 * 10 + int(version1[i])
                i += 1
            while j < n2 and version2[j] != '.':
                v2 = v2 * 10 + int(version2[j])
                j += 1
            i += 1
            j += 1
            if v1>v2: return 1
            if v1<v2: return -1

        return 0

