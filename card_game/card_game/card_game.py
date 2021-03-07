n,m = map(int, input().split()) # n,m을 공백으로 받기

result = 0

for i in range(n):
    data = list(map(int, input().split()))

    min_value = min(data) # 현재 행에서 가장 작은 데이터 찾기
    result = max(result,min_value) # 그 중 가장 큰 데이터 찾기
print(result)
