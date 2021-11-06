from typing import List

class Solution:
    """
           Λ  
        [-----|]     
    [---------|---]  
        [-----|---]
            [-|---]
              |  [-----]  // 只有此时需要再来一根

    """
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if points == []:
            return 0
        points.sort(key=lambda x: x[1])
        end = points[0][1]
        arrow = 1

        for i in points[1:]:
            next_start = i[0]
            if next_start > end:
                arrow += 1
                end = i[1]
            
        return arrow
