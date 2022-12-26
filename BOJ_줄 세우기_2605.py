student_num = int(input())
number_pick = list(map(int, input().split()))
line = []

for i in range(student_num):
    line.insert(len(line)-number_pick[i], i+1)

for i in range(student_num):
    print(line[i], end=' ')