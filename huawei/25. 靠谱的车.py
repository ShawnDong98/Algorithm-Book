"""
程序员小明打了一辆出租车去上班。出于职业敏感,  他注意到这辆出租车的计费表有点问题,  总是偏大。出租车司机解释说他不喜欢数字4,  所以改装了计费表,  任何数字位置遇到数字4就直接跳过,  其余功能都正常。比如:23再多一块钱就变为25; 39再多一块钱变为50; 399再多一块钱变为500; 小明识破了司机的伎俩,  准备利用自己的学识打败司机的阴谋。给出计费表的表面读数,  返回实际产生的费用。

示例1:
输入 5
输出 4
说明: 5表示计费表的表面读数。4表示实际产生的费用其实只有4块钱。

示例2:
输入 17
输出 15
说明 : 17表示计费表的表面读数。15表示实际产生的费用其实只有15块钱。

示例3:
输入 100
输出 81
说明: 100表示计费表的表面读数。81表示实际产生的费用其实只有81块钱。
"""


inp = int(input())

cnt = 0

for i in range(inp):
    if "4" in str(i):
        cnt += 1
    
print(inp - cnt)
