N, K = map(int, input().split())

temperature = list(map(int, input().split()))

max_temperature = tmp_temperature = sum(temperature[0:K])
i = 0
j = K - 1

while j < N - 1:
    j += 1
    tmp_temperature += temperature[j] - temperature[i]
    i += 1

    if max_temperature < tmp_temperature:
        max_temperature = tmp_temperature

print(max_temperature)
