def solve(n: int, a: int) -> int:
    #time complexity: O(N^3)
    used = [False for _ in range(n + 1)]
    used[a] = True
    places = [a]
    for _ in range(n - 1):
        now = 0
        m = -1
        for i in range(1, n + 1):
            if used[i]:
                continue
            dis = 1000000000
            for j in range(1, n + 1):
                if not used[j]:
                    continue
                dis = min(dis, abs(i - j))
            if m < dis:
                now = i
                m = dis
        used[now] = True
        places.append(now)
        
    res = 0
    for i in range(len(places)):
        if i % 2 == 0:
            continue
        res += places[i]
    return res

import sys
if __name__ == "__main__":
    for line in sys.stdin:
        n, a = map(int, line.split())
        ans = solve(n, a)
        print(ans)
