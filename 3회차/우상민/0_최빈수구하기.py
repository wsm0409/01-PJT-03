import sys

sys.stdin = open("_최빈수구하기.txt")

T = int(input())
for i in range(1, T+1):
    TC = int(input())
    N = list(map(int, (input().split())))
    counter = {}
    for idx in sorted(N):
        try: counter[idx] += 1
        except: counter[idx] = 1
    print(f'#{TC}', max([x for x, v in counter.items() if max(counter.values()) == v]))
