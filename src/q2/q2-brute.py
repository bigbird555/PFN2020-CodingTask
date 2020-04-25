s = ['' for _ in range(51)]
s[1] = 'a'
s[2] = 'b'
s[3] = 'c'
for tk in range(4, 11):
    s[tk] = s[tk - 3] + s[tk - 2] + s[tk - 1]

import sys
if __name__ == "__main__":
    for line in sys.stdin:
        k, p, q = map(int, line.split())
        target = s[k][p-1:q]
        a = target.count("a")
        b = target.count("b")
        c = target.count("c")
        print('a:{},b:{},c:{}'.format(a, b, c))
