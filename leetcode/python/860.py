from collections import defaultdict
from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dic = defaultdict(int)
        for i in bills:
            dic[i] += 1
            diff = i - 5
            # 如果需要找零
            while diff:
                # 如果找零大于等于10块， 并且有10块的零钱
                if diff >= 10 and dic[10]:
                    dic[10] -= 1
                    diff -= 10
                # 如果找零大于等于5块， 并且有5块的零钱
                elif diff >= 5 and dic[5]:
                    dic[5] -= 1
                    diff -= 5
                else:
                    return False
        return True