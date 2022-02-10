import collections
def bfs(begin):
    queue = collections.deque([begin])
    dis = collections.defaultdict(lambda:0)

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    end = '12345678x'

    while queue:
        state = queue.popleft()

        if state == end:
            return dis[state]

        for k, v in enumerate(state):
            if v == 'x':
                break

        x, y = k // 3, k % 3
        for dx, dy in directions:
            xhat, yhat = x + dx, y + dy
            temp_state = list(state)
            if 0 <= xhat < 3 and 0 <= yhat < 3:
                temp_state[xhat * 3 + yhat], temp_state[k] = temp_state[k], temp_state[xhat * 3 + yhat]
                new_state = ''.join(temp_state)
                if new_state not in dis:
                    dis[new_state] = dis[state] + 1
                    queue.append(new_state)
    return -1


inp = ''.join(input().split())
print(bfs(inp))
