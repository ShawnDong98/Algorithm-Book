"""
实现一个模拟目录管理功能的软件, 输入一个命令序列, 输出最后一条命令运行结果。支持命令: 

1) 创建目录命令: mkdir 目录名称, 如mkdir abc为在当前目录创建abc目录, 如果已存在同名目录则不执行任何操作。此命令无输出。

2) 进入目录命令: cd 目录名称, 如cd abc为进入abc目录, 特别地, cd ..为返回上级目录, 如果目录不存在则不执行任何操作。此命令无输出。

3) 查看当前所在路径命令: pwd, 输出当前路径字符串。

约束: 

1) 目录名称仅支持小写字母; mkdir和cd命令的参数仅支持单个目录, 如: mkdir abc和cd abc; 不支持嵌套路径和绝对路径, 如mkdir abc/efg, cd abc/efg, mkdir /abc/efg, cd /abc/efg是不支持的。

2) 目录符号为/, 根目录/作为初始目录。

3) 任何不符合上述定义的无效命令不做任何处理并且无输出。

输入描述: 
输入N行字符串, 每一行字符串是一条命令。

输出描述: 
输出最后一条命令运行结果字符串。

示例1: 
输入: 

mkdir abc
cd abc
pwd

输出: 
/abc/

说明: 
在根目录创建一个abc的目录, pwd 命令输出当前目录的路径。
"""

import sys

class DirectoryManager:
    def __init__(self):
        self.root = {'/': {}}
        self.current_path = ['/']
        self.current_dir = self.root['/']

    def mkdir(self, dirname):
        if dirname not in self.current_dir:
            self.current_dir[dirname] = {}

    def cd(self, dirname):
        if dirname == "..":
            if len(self.current_path) > 1:
                self.currnet_path.pop()
                self.current_dir = self._get_directory(self.current_path)
        elif dirname in self.current_dir:
            self.current_path.append(dirname)
            self.current_dir = self.current_dir[dirname]


    def pwd(self):
        return '/' + '/'.join(self.current_path[1:]) + '/'
    
    def _get_directory(self, path):
        dir_ref = self.root['/']
        for dir_name in path[1:]:
            dir_ref = dir_ref[dir_name]

        return dir_ref
    
    def process_command(self, command):
        parts = command.split()
        if len(parts) == 0:
            return 
        cmd = parts[0]
        if cmd == "mkdir" and len(parts) == 2:
            dirname = parts[1]
            if dirname.islower():
                self.mkdir(dirname)
        elif cmd == "cd" and len(parts) == 2:
            dirname = parts[1]
            if dirname.islower() or dirname == "..":
                self.cd(dirname)
        elif cmd == "pwd" and len(parts) == 1:
            return self.pwd()

input = sys.stdin.read     
commands = input().strip().split("\n")
manager = DirectoryManager()
result = None
    
for command in commands:
    result = manager.process_command(command)

if result:
    print(result)