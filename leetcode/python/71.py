class Solution:
    def simplifyPath(self, path: str) -> str:
        res = ""
        name = ""
        if path[-1] != '/': path += '/'
        for c in path:
            if c != '/': name += c
            else:
                if name == "..":
                    while len(res) and res[-1] != '/': res = res[:-1]
                    if len(res): res = res[:-1]
                elif name != '.' and name != '':
                    res += '/' + name
                name = ""

        if len(res) == 0: res = "/"
        return res
