def solution(n, stages):
    # [스테이지 번호, 실패율]을 저장할 리스트 생성
    fail_rate = []
    # 각 스테이지의 [현재 스테이지에 도달한 사람의 수, 현재 스테이지에 실패한 사람의 수]를 저장할 리스트 생성
    lst = [[0, 0]]
    # 1 단계부터  n 단계까지에 대한 도달한 사람의 수와 실패한 사람의 수 계산
    for i in range(1, n+1):
        # 현재 스테이지에 도달한 사람의 수
        achieve_stage = 0
        # 현재 스테이지에 실패한 사람의 수
        fail = 0
        # 사용자가 도달한 스테이지
        for j in stages:
            # 사용자가 도달한 스테이지가 i 번째 스테이지보다 클 경우
            if i <= j:
                # 현재 스테이지의 도달한 사람 수 ++
                achieve_stage += 1
                # 사용자가 도달한 스테이지가 i 번째 스테이지와 같을 경우
                if i == j:
                    # 현재 스테이지의 실패한 사람 수 ++
                    fail += 1
        # 리스트에 [현재 스테이지에 도달한 사람의 수, 현재 스테이지에 실패한 사람의 수] 리스트 추가
        lst.append([achieve_stage, fail])
    # 1 단계부터 n 단계까지의 실패율 계산
    for i in range(1, n+1):
        # 현재 스테이지에 도달한 사람이 있을 경우
        if lst[i][0] != 0:
            # fail_rate 리스트에 [현재 스테이지, 실패율] 리스트 추가
            fail_rate.append([i, lst[i][1]/lst[i][0]])
        # 현재 스테이지에 도달한 사람이 없을 경우
        else:
            # 실패율 0으로 정의하여 fail_rate 리스트에 [현재 스테이지, 0] 리스트 추가
            fail_rate.append([i, 0])
    # fail_rate 리스트를 실패율을 기준으로 내림차순 정렬
    fail_rate.sort(key=lambda x: x[1], reverse=True)
    # fail_rate 리스트의 결과에 대한 스테이지 값만 반환
    return [s[0] for s in fail_rate]
# 예제
print(solution(5, [2,1,2,6,2,4,3,3]))