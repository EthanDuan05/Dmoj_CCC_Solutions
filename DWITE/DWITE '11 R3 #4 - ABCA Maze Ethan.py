N = 0
line = []
for _ in range(10):
    line.append(list(input()))

N = len(line[0])

Graph = [['#' for j in range(N + 2)] for i in range(10 + 2)]

for i in range(10):
    Graph[i+1] = Graph[i+1][:1] + line[i] + Graph[i+1][-1:]


def find_starting(character):
    for i in range(1, 10+1):
        if character in Graph[i]:
            return i, Graph[i].index(character)


def bfs(graph, r, c, x, y):
    visited = [[False for j in range(N + 2)] for i in range(10 + 2)]
    level = [[-1 for j in range(N + 2)] for i in range(10 + 2)]
    # visited[x][y] = True
    level[x][y] = 0
    queue = []
    queue.append((x, y))
    direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    while queue:
        row_, col_ = queue.pop(0)
        queue.append((row_, col_))
        for d_r, d_c in direction:
            current_r = d_r + row_
            current_c = d_c + col_
            if visited[current_r][current_c]: continue
            if graph[current_r][current_c] == '#': continue
            visited[current_r][current_c] = True
            queue.append((current_r, current_c))
            level[current_r][current_c] = level[row_][col_] + 1
            if current_r == r and current_c == c:
                return level[r][c]

    return -1


for _ in range(5):
    cnt = 0
    line = list(input())
    if len(line) == 1:
        print(0)
    else:
        cnt = 0
        a = line[0]
        b = ''

        ans = 0
        for i in range(1, len(line)):
            b = line[i]

            if a == b:
                continue

            start = find_starting(a)
            final = find_starting(b)

            start_x = int(start[0])
            start_y = int(start[1])

            final_x = int(final[0])
            final_y = int(final[1])

            ans += (bfs(Graph, final_x, final_y, start_x, start_y))

            a = b

        print(ans)