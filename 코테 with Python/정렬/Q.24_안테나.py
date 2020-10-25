# 집의 개수 입력
n = int(input())
# 집 위치 입력 후 오름차순 정렬
lst = sorted(list(map(int, input().split())))
# 리스트의 중간값 출력
print(lst[(n-1)//2])
