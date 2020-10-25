# 수열에 속해 있는 개수 입력
n = int(input())
# n 개의 정수를 입력 받아 리스트에 저장
lst = []
for _ in range(n):
    lst.append(int(input()))
# 리스트 내림차순으로 정렬
lst.sort(reverse=True)
# 리스트 출력
for i in range(n):
    print(lst[i], end=' ')
