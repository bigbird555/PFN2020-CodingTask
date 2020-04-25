l = [0 for _ in range(51)]
for i in range(51):
    if i == 0:
        continue
    elif i < 4:
        l[i] = 1
    else:
        l[i] = l[i - 3] + l[i - 2] + l[i - 1]
na = [0 for _ in range(51)]
nb = [0 for _ in range(51)]
nc = [0 for _ in range(51)]
na[1] = nb[2] = nc[3] = 1
for i in range(51):
    if i < 4:
        continue
    else:
        na[i] = na[i - 3] + na[i - 2] + na[i - 1]
        nb[i] = nb[i - 3] + nb[i - 2] + nb[i - 1]
        nc[i] = nc[i - 3] + nc[i - 2] + nc[i - 1]

def dfs(k: int, p: int, q: int):
    a = 0
    b = 0
    c = 0
    if k == 1:
        return 1, 0, 0
    elif k == 2:
        return 0, 1, 0
    elif k == 3:
        return 0, 0, 1
    else:
        if q - p + 1 == l[k]:
            return na[k], nb[k], nc[k]
        if p <= l[k - 3]:
            ta, tb, tc = dfs(k - 3, p, min(l[k - 3], q))
            a += ta
            b += tb
            c += tc
        if p <= l[k - 3] + l[k - 2] and q > l[k - 3]:
            ta, tb, tc = dfs(k - 2, max(1, p - l[k - 3]), min(l[k - 2], q - l[k - 3]))
            a += ta
            b += tb
            c += tc
        if q > l[k - 3] + l[k - 2]:
            ta, tb, tc = dfs(k - 1, max(1, p - l[k - 3] - l[k - 2]), q - l[k - 3] - l[k - 2])
            a += ta
            b += tb
            c += tc
    return a, b, c

import sys
if __name__ == "__main__":
    for line in sys.stdin:
        k, p, q = map(int, line.split())
        a, b, c = dfs(k, p, q)
        #print(l[k])
        print('a:{},b:{},c:{}'.format(a, b, c))
