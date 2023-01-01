rlt = 0
matrix = [[0] * 100 for _ in range(100)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for y in range(y1, y2):
        for x in range(x1, x2):
            matrix[y][x] = 1

for r in range(len(matrix)):
    for c in range(len(matrix)):
        if matrix[r][c]:
            rlt += 1

print(rlt)