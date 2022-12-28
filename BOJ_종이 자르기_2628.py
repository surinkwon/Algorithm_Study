width, height = map(int, input().split())

line_num = int(input())

max_width = max_height = 0
w_list = [0, width]
h_list = [0, height]

for _ in range(line_num):
    d, num = map(int, input().split())

    if d:
        w_list.append(num)
    else:
        h_list.append(num)

# 가장 큰 가로길이, 세로길이 찾기
w_list.sort()
h_list.sort()

for i in range(1, len(w_list)):
    max_width = max(max_width, w_list[i]-w_list[i-1])

for i  in range(1, len(h_list)):
    max_height = max(max_height, h_list[i]-h_list[i-1])

print(max_height*max_width)