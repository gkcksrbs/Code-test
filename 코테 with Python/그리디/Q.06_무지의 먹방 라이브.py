from _collections import deque
import heapq

# 효율성 구데기(시간 초과)
# def solution(food_times, k):
#     if sum(food_times) <= k:
#         return -1
#
#     D = deque()
#     answer = 0
#
#     for i in range(len(food_times)):
#         D.append([i+1, food_times[i]])
#
#     for i in range(k):
#         while True:
#             if D[0][1] != 0:
#                 break
#             D.append(D.popleft())
#
#         D[0][1] -= 1
#         D.append(D.popleft())
#
#     while True:
#         if D[0][1] != 0:
#             break
#         D.append(D.popleft())
#
#     answer = D[0][0]
#
#     return answer

# 이것도 효율성 구데기 (시간 초과)
# def solution(food_times, k):
#     if sum(food_times) <= k:
#         return -1
#
#     D = deque()
#     answer = 0
#
#     if k >= len(food_times) * min(food_times):
#         k -= len(food_times) * min(food_times)
#         Min = min(food_times)
#         for i in range(len(food_times)):
#             food_times[i] -= Min
#
#     for i in range(len(food_times)):
#         if food_times[i] == 0:
#             continue
#         D.append([i + 1, food_times[i]])
#
#     for i in range(k):
#         while True:
#             if D[0][1] != 0:
#                 break
#             D.append(D.popleft())
#
#         D[0][1] -= 1
#         D.append(D.popleft())
#
#     while True:
#         if D[0][1] != 0:
#             break
#         D.append(D.popleft())
#
#     answer = D[0][0]
#
#     return answer

# ㅅㅂ
# def solution(food_times, k):
#     if sum(food_times) <= k:
#         return -1
#
#     new_food_times = []
#     for i in range(len(food_times)):
#         new_food_times.append([food_times[i], i+1])
#
#     while k >= len(new_food_times) * min(new_food_times)[0]:
#         Min = min(new_food_times)[0]
#         k -= len(new_food_times) * Min
#
#         for i in range(len(new_food_times)):
#             new_food_times[i][0] -= Min
#
#         heapq.heapify(new_food_times)
#
#         while new_food_times[0][0] == 0:
#             heapq.heappop(new_food_times)
#     if k == 0:
#         return new_food_times[]
#     return new_food_times[len(new_food_times) % k][1]

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    new_food_times = []
    for i in range(len(food_times)):
        new_food_times.append((food_times[i], i+1))
    heapq.heapify(new_food_times)

    sum_time = 0
    prev = 0
    food = len(food_times)

    while sum_time + ((new_food_times[0][0] - prev) * food) <= k:
        now = heapq.heappop(new_food_times)[0]
        sum_time += (now - prev) * food
        food -= 1
        prev = now

    result = sorted(new_food_times, key= lambda x: x[1])
    return result[(k - sum_time) % food][1]

print(solution([3,1,2], 5))