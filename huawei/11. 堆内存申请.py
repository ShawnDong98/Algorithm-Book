"""
有一个总空间为100字节的堆, 现要从中新申请一块内存, 内存分配原则为优先紧接着前一块已使用内存分配空间足够且最接近申请大小的空闲内存。

输入描述

第1行是1个整数, 表示期望申请的内存字节数。

第2到第N行是用空格分割的两个整数, 表示当前已分配的内存的情况, 每一行表示一块已分配的连续内存空间, 每行的第1个和第2个整数分别表示偏移地址和内存块大小, 如: 0 1 3 2 表示0偏移地址开始的1个字节和3偏移地址开始的2个字节已被分配, 其余内存空闲。

输出描述

若申请成功, 输出申请到内存的偏移 若申请失败, 输出-1。

备注 1.若输入信息不合法或无效, 则申请失败

2.若没有足够的空间供分配, 则申请失败

3.堆内存信息有区域重叠或有非法值等都是无效输入

示例1


输入：
1
0 1
3 2

输出：
1

说明：
堆中已使用的两块内存是偏移从0开始的1字节和偏移从3开始的2字节, 空闲的两块内存是偏移从1开始2个字节和偏移从5开始95字节根据分配原则, 新申请的内存应从1开始分配1个字节, 所以输出偏移为1。
"""

def allocate_memory(addr_block):
    total_size = 100

    for i in range(len(addr_block)):
        addr, block = addr_block[i]
        if addr < 0 or block <= 0 or addr + block >= total_size:
            return -1
        elif i > 0 and addr_block[i][0] < addr_block[i-1][0] + addr_block[i][1]:
            return -1
        
    free_block = []
    current_start = 0

    for addr, block in addr_block:
        if addr > current_start:
            free_block.append((current_start, addr - current_start))

        current_start = addr + block

    if current_start < total_size:
        free_block.append((current_start, total_size - current_start))


    best_fit = 0
    for addr, block in free_block:
        if not best_fit or block < best_fit[1]:
            best_fit =  (addr, block)
        
    if best_fit:
        return best_fit[0]
    else:
        return -1
    


n = int(input())
addr_block = []


while True:
    try:
        addr, block= map(int, input().split())
        addr_block.append((addr, block))
    except:
        break

print(allocate_memory(addr_block))



