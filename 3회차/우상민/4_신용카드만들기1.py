import sys

sys.stdin = open("_신용카드만들기1.txt")

T = int(input())
for i in range(1, T+1):
    N = input().split()
    count = 0
    for idx in range(0, 15):
        if (idx+1) % 2 == 0:
            count += int(N[idx])
        elif (idx+1) % 2 == 1:
            count += int(N[idx])*2
    if count % 10 == 0:
        print(f'#{i}', 0)
    elif count % 10 == 1:
        print(f'#{i}', 9)
    elif count % 10 == 2:
        print(f'#{i}', 8)
    elif count % 10 == 3:
        print(f'#{i}', 7)
    elif count % 10 == 4:
        print(f'#{i}', 6)
    elif count % 10 == 5:
        print(f'#{i}', 5)
    elif count % 10 == 6:
        print(f'#{i}', 4)
    elif count % 10 == 7:
        print(f'#{i}', 3)
    elif count % 10 == 8:
        print(f'#{i}', 2)
    elif count % 10 == 9:
        print(f'#{i}', 1)