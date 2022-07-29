import sys

sys.stdin = open("_문자열의거울상.txt")

T = int(input())

for i in range(1, T+1):
    li = []
    N = str(input())
    for idx in N:
        if idx == 'd':
            li.append('b')
        elif idx == 'b':
            li.append('d')
        elif idx == 'q':
            li.append('p')
        else: 
            li.append('q')
    print(f'#{i}', ''.join(li[::-1]))