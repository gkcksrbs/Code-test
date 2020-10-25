import heapq
# 숫자 카드 묶음 개수 입력
n = int(input())
# 힙에 카드 묶음 입력
lst = []
for _ in range(n):
    heapq.heappush(lst, int(input()))
# 힙의 원소가 1개일 경우 비교할 필요 없으므로 0 출력
if n == 1:
    print(0)
# 힙의 원소의 개수가 1개가 아닐 경우
else:
    result = 0
    # 힙에 원소의 개수가 1개일 때까지
    while len(lst) > 1:
        # 가장 작은 카드 묶음 2개 꺼내기
        min1 = heapq.heappop(lst)
        min2 = heapq.heappop(lst)

        result += min1 + min2
        # 가장 작은 카드 묶음 2개를 더해서 다시 힙에 삽입
        heapq.heappush(lst, min1+min2)
    # 결과 출력
    print(result)
