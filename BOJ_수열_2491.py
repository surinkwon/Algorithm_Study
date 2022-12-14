# N 입력
N = int(input())

# 수열 입력
numbers = list(map(int, input().split()))
max_length = 1
tmp_length = 1

# 오름차순 검사
for i in range(1, len(numbers)):
    if numbers[i] >= numbers[i - 1]:
        tmp_length += 1
    else:
        max_length = max(max_length, tmp_length)
        tmp_length = 1

max_length = max(max_length, tmp_length)

tmp_length = 1

# 내림차순 검사
for i in range(1, len(numbers)):
    if numbers[i] <= numbers[i - 1]:
        tmp_length += 1
    else:
        max_length = max(max_length, tmp_length)
        tmp_length = 1

max_length = max(max_length, tmp_length)

print(max_length)