# 브루트포스

# 옆면 합 구하는 함수
def sideSum(total, bottom, top):
    if max(bottom, top) != 6:
        total += 6
    elif 5 not in [bottom, top]:
        total += 5
    else:
        total += 4
    
    return total

# 주사위 개수
N = int(input())

DICE = []
max_sum = tmp_sum = 0
opposite_index = [5, 3, 4, 1, 2, 0]

# 주사위 입력
for _ in range(N):
    DICE.append(list(map(int, input().split())))

# 한 면씩 돌면서 검사
for bottom_idx in range(6):
    tmp_sum = 0
    bottom = DICE[0][bottom_idx]
    top = DICE[0][opposite_index[bottom_idx]]

    tmp_sum = sideSum(tmp_sum, bottom, top)
    
    # 주사위 하나씩 위아래 찾고 사이드 더하기
    for dice_idx in range(1, N):
        new_bottom_idx = DICE[dice_idx].index(top)
        bottom = DICE[dice_idx][new_bottom_idx]
        top = DICE[dice_idx][opposite_index[new_bottom_idx]]

        tmp_sum = sideSum(tmp_sum, bottom, top)
    
    if max_sum < tmp_sum:
        max_sum = tmp_sum

print(max_sum)
