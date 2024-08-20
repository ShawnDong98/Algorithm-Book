"""
疫情期间, 需要大家保证一定的社交距离, 公司组织开交流会议, 座位有一排共N个座位, 编号分别为[0..N-1], 要求员工一个接着一个进入会议室, 并且可以在任何时候离开会议室。

满足: 每当一个员工进入时, 需要坐到最大社交距离的座位(例如: 位置A与左右有员工落座的位置距离分别为2和2, 位置B与左右有员工落座的位置距离分别为2和3, 影响因素都为2个位置, 则认为座位A和B与左右位置的社交距离是一样的); 如果有多个这样的座位, 则坐到索引最小的那个座位。

输入

会议室座位总数seatNum, (1 ≤ seatNums ≤ 500)

员工的进出顺序seatOrLeave数组, 元素值为1: 表示进场; 元素值为负数, 表示出场(特殊: 位置0的员工不会离开), 例如-4表示坐在位置4的员工离开(保证有员工坐在该座位上)

输出

最后进来员工, 他会坐在第几个位置, 如果位置已满, 则输出-1

样例输入

10
[1, 1, 1, 1, -4, 1]

样例输出

5
"""

def find_seat(seatNum, seatOrLeave):
    seats = [0] * seatNum

    def find_max_distance_seat():
        max_distance = -1
        best_seat = -1

        for i in range(seatNum):
            if seats[i] == 0:
                left_distance = right_distance = seatNum

                for left in range(i-1, -1, -1):
                    if seats[left] == 1:
                        left_distance = i - left
                        break
                
                for right in range(i+1, seatNum):
                    if seats[right] == 1:
                        right_distance = right - i
                        break
                
                distance = min(left_distance, right_distance)

                if distance > max_distance:
                    max_distance = distance
                    best_seat = i

        return best_seat

    last_seat = -1
    for action in seatOrLeave:
        if action == 1:
            seat = find_max_distance_seat()
            if seat == -1:
                return -1
            seat[seat] = 1
            last_seat = seat
        else:
            seat_to_leave = -action
            seats[seat_to_leave] = 0

    return last_seat
                


seatNum = int(input())

seatOrLeave = input().split()


