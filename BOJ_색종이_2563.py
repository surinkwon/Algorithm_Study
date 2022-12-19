# 색종이 개수
N = int(input())

# 도화지, 색종이 넓이
sketchbook = [[0] * 100 for _ in range(100)]
paper = 10

# 도화지에 색종이 붙이기
for _ in range(N):
    left, bottom = map(int, input().split())

    for r in range(len(sketchbook) - paper - bottom, len(sketchbook) - bottom):
        for c in range(left, left + paper):
            sketchbook[r][c] = 1

# 색종이 붙은 면적 구하기
total = 0

for r in range(len(sketchbook)):
    for c in range(len(sketchbook)):
        if sketchbook[r][c]:
            total += 1

print(total)