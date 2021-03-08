n,m,k = map(int,input().split()) # n,m,k를 공백으로 구분받기 
data = list(map(int,input().split())) # n개의 수를 공백으로 구분받기

data.sort() # 입력받은 수 정렬하기
first = data[n-1]
second = data[n-2]
result = 0 

while True:
    for i in range(k): # 가장 큰 수를 k번 더하기 
        if m == 0: # m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1 # 횟수 차감 
    if m==0:
        break
    result += second 
    m -= 1
print(result) # 답안 출력 