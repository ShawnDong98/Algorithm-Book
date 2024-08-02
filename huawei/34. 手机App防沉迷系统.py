"""
智能手机方便了我们生活的同时, 也侵占了我们不少的时间。手机App防沉迷系统能够让我们每天合理的规划手机App使用时间, 在正确的时间做正确的事。它的大概原理是这样的:

1、在一天24小时内, 可注册每个App的允许使用时段;

2、一个时段只能使用一个App, 举例说明:不能同时在09:00-10:00注册App2和App3;

3、App有优先级, 数值越高, 优先级越高。注册使用时段时, 如果高优先级的App时间和低优先级的时段有冲突, 则系统会自动注销低优先级的时段;如果App的优先级相同, 则后添加的App不能注册。

举例1:

1、注册App3前:

2、App3注册时段和App2有冲突:

3、App3优先级高, 系统接受App3的注册, 自动注销App2的注册:

举例2:

1、注册App4:

2、App4和App2及App3都有冲突, 优先级比App2高, 但比App3低, 这种场景下App4注册不上, 最终的注册效果如下:

4、一个App可以在一天内注册多个时段。

请编程实现, 根据输入数据注册App, 并根据输入的时间点, 返回该时间点可用的App名称, 如果该时间点没有注册任何App, 请返回字符串NA。

输入描述
第一行表示注册的App数N (N≤100)

第二部分包括N 行, 每行表示一条App注册数据

最后一行输入一个时间点, 程序即返回注册点的App

2
App1 1 09:00 10:00
App2 2 11:00 11:30
09:30
数据说明如下
1、N行注册数据以空格分隔, 四项数依次表示: App名称、优先级、起始时间, 结束时间
2.优先级1-5, 数字值越大, 优先级越高
3、时间格式HH:MM, 小时和分钟都是两位, 不足两位前面补0
4.起始时间需小于结束时间, 否则注册不上
5.注册信息中的时间段包含起始时间点, 不包含结束时间点

输出描述
输出一个字符串, 表示App名称, 或NA表示空闲时间。

示例1
输入:
1
App1 1 09:00 10:00
09:30

输出:
App1

说明:
App1注册在9点到10点间, 9点半可用的应用名是App1

示例2
输入:
2
App1 1 09:00 10:00
App2 2 09:10 09:30
09:20

输出:
App2

说明:
ApP1和App2的时段有冲突, App2优先级高,注册App2之后, App1自动注销, 因此输出App2

示例3
输入:
2
App1 1 09:00 10:00
App2 2 09:10 09:30
09:50

输出:
NA
"""



time_table = [None] * 24 * 60 
N = int(input())

for _ in range(N):
    name, priority, start, end = input().split()
    start = int(start[:2]) * 60 + int(start[-2:])
    end = int(end[:2]) * 60 + int(end[-2:])
    print(start)
    print(end)
    for i in range(start, end):
        if time_table[i] is not None:
            if priority > time_table[i][1]:
                time_table[i] = (name, priority)
        else:
            time_table[i] = (name, priority)
    

time = input()
time = int(time[:2]) * 60 + int(time[-2:])
print(time)

if time_table[time] is None:
    print("NA")
else:
    print(time_table[time][0])