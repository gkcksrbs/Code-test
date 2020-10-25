# 학생 수 입력
n = int(input())
# 학생의 정보를 입력 받아 리스트에 저장
lst = []
for _ in range(n):
    data = input().split()
    lst.append([data[0], int(data[1]), int(data[2]), int(data[3])])
# 국어 점수 내림차순, 영어 점수 오름차순, 수학 점수 내림차순, 이름 순으로 정렬
lst.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
# 결과 출력
for i in range(len(lst)):
    print(lst[i][0])
