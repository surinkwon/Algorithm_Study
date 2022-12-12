# 참외 수
K = int(input())

# 방향, 길이 입력
direction = []
length = []

for _ in range(6):
    d, l = map(int, input().split())
    direction.append(d)
    length.append(l)

# 큰 사각형, 작은 사각형 면적
big_square = 1
small_square = 1

for i in range(6):
    d = direction[i]

    # 방향이 한 번 나오면 큰 사각형
    if direction.count(d) == 1:
        big_square *= length[i]
    
    # 두 번 나오면서 가운데 껴있는 게 작은 사각형 길이
    elif (direction.count(direction[(i + 2) % 6]) == 1 and direction.count(direction[(i + 1) % 6]) == 2) or (direction.count(direction[(i + 4) % 6]) == 1 and direction.count(direction[(i + 5) % 6]) == 2):
        small_square *= length[i]

print((big_square-small_square)*K)