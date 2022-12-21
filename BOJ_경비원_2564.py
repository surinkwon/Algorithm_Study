# 최단거리 구하는 함수
def calLen(store_direction, store_len):
    if dong_direction == store_direction:
        return abs(dong_len - store_len)
    
    if (dong_direction == 1 or dong_direction == 2) and (store_direction == 1 or store_direction == 2):
        return min(dong_len+store_len, 2 * WIDTH - dong_len - store_len) + HEIGHT
    
    if (dong_direction == 3 or dong_direction == 4) and (store_direction == 3 or store_direction == 4):
        return min(dong_len+store_len, 2 * HEIGHT - dong_len - store_len) + WIDTH
    
    if (dong_direction == 1 and store_direction == 4):
        return WIDTH - dong_len + store_len 

    if (dong_direction == 4 and store_direction == 1):
        return dong_len + WIDTH - store_len

    if (dong_direction == 1 and store_direction == 3) or (dong_direction == 3 and store_direction == 1):
        return dong_len + store_len

    if (dong_direction == 2 and store_direction == 4) or (dong_direction == 4 and store_direction == 2):
        return WIDTH - dong_len + HEIGHT - store_len

    if (dong_direction == 2 and store_direction == 3):
        return dong_len + HEIGHT - store_len
        
    if (dong_direction == 3 and store_direction == 2):
        return HEIGHT - dong_len + store_len

# 가로, 세로
WIDTH, HEIGHT = map(int, input().split())

# 상점 개수, 상점
store_num = int(input())
stores = []
total = 0

# 상점 위치 입력
for _ in range(store_num):
    stores.append(list(map(int, input().split())))

# 동근이 위치
dong_direction, dong_len = map(int, input().split())

for i in range(store_num):
    store_direction, store_len = stores[i]

    total += calLen(store_direction, store_len)

print(total)
