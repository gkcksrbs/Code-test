# 원소의 개수, 바꿔치기 개수 입력
n, k = map(int, input().split())
# 배열 a, b 의 원소 입력 받고 배열 a 는 오름차순, 배열 b 는 내림차순으로 정렬
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())), reverse=True)
# 두 배열의 원소 비교
for i in range(k):
    # a 의 원소가 b 의 원소보다 작을 경우
    if a[i] < b[i]:
        # 두 원소 교체
        a[i], b[i] = b[i], a[i]
    # 다음 반복문부터 a 의 원소가 더 크므로 반복문 탈출
    else:
        break
# a 리스트의 모든 원소 합 출력
print(sum(a))
