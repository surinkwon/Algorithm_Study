# 수 입력, 출력 변수
N = int(input())
rlt_list = []
max_num = 0

# 수 하나씩 돌아가면서 검사
for num in range(N, 0, -1):
    num_list = [N, num]

    while num_list[len(num_list)-1] >= 0:
        num_list.append(num_list[len(num_list)-2]-num_list[len(num_list)-1])
    
    if max_num < len(num_list) - 1:
        max_num = len(num_list) - 1
        rlt_list = num_list[0:len(num_list)-1]

print(max_num)

for i in range(len(rlt_list)):
    print(rlt_list[i], end=' ')