# 면적 계산 함수
def calArea(pillars):
    cur_max_height = pillars[0][1]
    area = x_cnt = 0

    for i in range(1, N):
        if cur_max_height == max_height:
            break

        x = pillars[i][0] - pillars[i - 1][0]
        area += cur_max_height * abs(x)
        x_cnt += abs(x)

        if cur_max_height < pillars[i][1]:
            cur_max_height = pillars[i][1]

    return area, x_cnt


# 기둥 수, 기둥 리스트, 면적
N = int(input())
pillars = []
total_area = max_height = total_x = 0

# 기둥 입력받기
for _ in range(N):
    pillar = list(map(int, input().split()))

    # 가장 높은 기둥 찾기
    if max_height < pillar[1]:
        max_height = pillar[1]

    pillars.append(pillar)

# 왼쪽 면적 더하기
pillars.sort(key=lambda x: x[0])

area, x_cnt = calArea(pillars)

total_area += area
total_x += x_cnt

# 오른쪽 면적 더하기
pillars.sort(key=lambda x: -x[0])

area, x_cnt = calArea(pillars)

total_area += area
total_x += x_cnt

# 가장 높은 기둥 면적 더하기
total_area += (pillars[0][0] - pillars[len(pillars)-  1][0] + 1 - total_x) * max_height

print(total_area)