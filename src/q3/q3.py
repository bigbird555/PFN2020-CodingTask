def solve(n: int, a: int) -> int:
    #n, a = map(int, input().split())
    used = [False for i in range(n + 1)]
    used[a] = True
    places = [a]
    import heapq
    h = []
    heapq.heapify(h) #(v, i, l, r)
    if a != n:
        heapq.heappush(h, (-(n - a), n, a, -1))
    if a != 1:
        heapq.heappush(h, (-(a - 1), 1, -1, a))
    while h:
        t = heapq.heappop(h)
        v, i, l, r = t
        if used[i]:
            continue
        used[i] = True
        places.append(i)
        if l != -1:
            nl = (l + i) // 2
            heapq.heappush(h, (-(nl - l), nl, l, i))
        if r != -1:
            nr = (i + r) // 2
            heapq.heappush(h, (-(nr - i), nr, i, r))
            
    res = 0
    for i in range(len(places)):
        if i % 2 != 0:
            res += places[i]
    return res

import sys
if __name__ == "__main__":
    
    for line in sys.stdin:
        n, a = map(int, line.split())
        ans = solve(n, a)
        print(ans)
