from bisect import bisect_right, bisect_left
# '?'가 접미사에 있을 때 길이별로 저장하기 위한 리스트 생성
lst = [[] for _ in range(10001)]
# '?'가 접두사에 있을 때 길이별로 뒤집어서 저장하기 위한 리스트 생성
reversed_lst = [[] for _ in range(10001)]
# left_val, right_val 사이에 있는 데이터의 개수를 반환하는 함수
def count_by_range(array, left_val, right_val):
    left_index = bisect_left(array, left_val)
    right_index = bisect_right(array, right_val)
    return right_index - left_index

def solution(words, queries):
    # 결과값
    answer = []
    # 모든 단어 탐색
    for word in words:
        # 해당 길이를 인덱스로 하는 리스트에 입력
        lst[len(word)].append(word)
        # 해당 길이를 인덱스로 하는 리스트에 뒤집어서 입력
        reversed_lst[len(word)].append(word[::-1])
    # 리스트 정렬
    for i in range(10001):
        lst[i].sort()
        reversed_lst[i].sort()
    # 쿼리 안의 모든 리스트 탐색
    for query in queries:
        # '?'가 접미사에 위치 하였을 경우
        if query[0] != '?':
            # 뒤집어 지지 않은 리스트 이분 탐색 실행
            cnt = count_by_range(lst[len(query)], query.replace('?', 'a'), query.replace('?', 'z'))
        # '?'가 접두사에 위치 하였을 경우
        else:
            # 뒤집어 진 리스트 이분 탐색 실행
            cnt = count_by_range(reversed_lst[len(query)], query[::-1].replace('?', 'a'), query[::-1].replace('?', 'z'))
        # 검색된 단어의 개수 저장
        answer.append(cnt)
    # 결과값 반환
    return answer
print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?", "?????"]))

