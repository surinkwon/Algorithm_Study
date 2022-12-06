'''
구현
'''

N = int(input())

switch_list = [0] + list(map(int, input().split()))
status_change = [1, 0]

K = int(input())

for _ in range(K):
    s, n = map(int, input().split())

    if s == 1:
        for i in range(n, N + 1, n):
            switch_list[i] = status_change[switch_list[i]]
    else:
        for i in range(1, N):
            if n - i <= 0 or n + i >= N + 1 or switch_list[n - i] != switch_list[n + i]:
                break
        i -= 1
        for j in range(n - i, n + i + 1):
            switch_list[j] = status_change[switch_list[j]]



for i in range(1, N + 1):
    print(switch_list[i], end=' ')
    if i % 20 == 0:
        print()