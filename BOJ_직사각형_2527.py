for _ in range(4):
    points = list(map(int, input().split()))
    rlt = 'a'

    # 왼쪽 아래 꼭짓점 기준 오른쪽에 있는 사각형이 3, 4
    if points[0] <= points[4]:
        x1, y1, x2, y2, x3, y3, x4, y4 = points
    else:
        x1, y1, x2, y2 = points[4:]
        x3, y3, x4, y4 = points[0:4]

    # 안 닿음
    if (x3 > x2 or y3 > y2 or y4 < y1):
        rlt = 'd'
    
    # 점
    elif x2 == x3 and (y1 == y4 or y2 == y3):
        rlt = 'c'

    # 선분
    elif x3 == x2 or y3 == y2 or y4 == y1:
        rlt = 'b'

    print(rlt)