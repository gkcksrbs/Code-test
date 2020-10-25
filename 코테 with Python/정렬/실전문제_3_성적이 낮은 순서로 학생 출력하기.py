# 학생 수 입력
n = int(input())
# n 명의 학생 정보를 입력받아 리스트에 저장
lst = []
for _ in range(n):
    data = input().split()
    lst.append([data[0], int(data[1])])
# 점수를 기준으로 오름차순 정렬
lst.sort(key=lambda score: score[1])
# 성적이 낮은 순으로 학생 이름 출력
for i in range(len(lst)):
    print(lst[i][0], end=' ')

