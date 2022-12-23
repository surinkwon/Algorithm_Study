# 철수 빙고판
bingo_board = {}
numbers = []
total_num = 0
bingo = [0] * 6
garo = [0] * 5
sero = [0] * 5
daegak = [0, 0]

for i in range(5):
    temp_list = list(map(int, input().split()))

    for j in range(5):
        bingo_board[temp_list[j]] = [i, j]

# 번호 저장
for _ in range(5):
    numbers.append(list(map(int, input().split())))

# 번호 부르기
for i in range(5):
    for j in range(5):
        r, c = bingo_board[numbers[i][j]]
        
        total_num += 1

        # 가로 세로 검사
        garo[r] += 1
        bingo[garo[r]] += 1

        sero[c] += 1
        bingo[sero[c]] += 1

        # 대각 검사
        if r + c == 4:
            daegak[1] += 1
            bingo[daegak[1]] += 1
        
        if r - c == 0:
            daegak[0] += 1
            bingo[daegak[0]] += 1
        
        if bingo[5] >= 3:
            break

    if bingo[5] >= 3:
        break

print(total_num)