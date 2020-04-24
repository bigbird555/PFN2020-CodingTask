def det3(a) -> int:
    res = 0
    for j in range(3):
        tmp = a[1][(j+1)%3] * a[2][(j+2)%3] - a[1][(j+2)%3] * a[2][(j+1)%3]
        tmp *= a[0][j]
        res += tmp
    return res

def solve(x: int, y: int, d:int) -> int:
    res = 0
    for k in range(1<<9):
        a = [[-1 for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                b = 3 * i + j
                if k>>b&1:
                    a[i][j] = x
                else:
                    a[i][j] = y
        tmpd = det3(a)
        if tmpd == d:
            res += 1
    return res

import sys
if __name__ == "__main__":
    
    for line in sys.stdin:
        x, y, d = map(int, line.split())
        ans = solve(x, y, d)
        print(ans)
