"""
公司用一个字符串来表示员工的出勤信息: 
absent: 缺勤
late: 迟到
leaveearly: 早退
present: 正常上班
现需根据员工出勤信息, 判断本次是否能获得出勤奖, 能获得出勤奖的条件如下: 
缺勤不超过一次; 没有连续的迟到早退; 任意连续7次考勤, 缺勤迟到早退不超过3次

输入描述

第一行输入一个整数`n`, 表示有多少个员工

后面`n`行, 每一行输入若干个字符串, 表示第`i`名员工的出勤信息

输出描述

输出`n`行, 每一行表示这名员工能否获得出勤奖, 如果可以, 则输出“true", 否则输出”false"

示例1

输入: 
2
present
present present

输出: 
true true


示例2

输入: 
2
present
present absent present present leaveearly present absent

输出: 
true false
"""
def func(inp):
    if inp.count('absent') > 1:
        return False
        
    for i in range(len(inp) - 1):
        if (inp[i] == "late" and inp[i+1] == "late") or (inp[i] == "late" and inp[i+1] == "leaveearly") or (inp[i] == "leaveearly" and inp[i+1] == "leaveearly") or (inp[i] == "leaveearly" and inp[i+1] == "late"):
            return False

    for i in range(len(inp)-6):
        window = inp[i:i+7]
        if window.count("absent") + window.count("late") + window.count("leaveearly") >= 3:
            return False
        
    return True


n = int(input())

for _ in range(n):
    inp = input().split()
    if func(inp):
        print("true")
    else:
        print("false")











