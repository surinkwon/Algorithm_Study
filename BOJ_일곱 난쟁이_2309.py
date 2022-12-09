from itertools import combinations

dwarf = []

# 키 입력받기
for _ in range(9):
    dwarf.append(int(input()))

dwarf.sort()
# 넘치는 키
exceed_height = sum(dwarf) - 100

# 두 명 뽑아서 넘치는 키와 같으면 걔네 빼기
pos = list(combinations(dwarf, 2))

for i in range(len(pos)):
    if sum(pos[i]) == exceed_height:
        for j in range(len(dwarf)):
            if dwarf[j] not in pos[i]:
                print(dwarf[j])
        
        break