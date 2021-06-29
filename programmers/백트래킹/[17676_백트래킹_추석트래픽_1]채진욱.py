# 백트래킹(backtracking)이란? :
# 해를 찾는 도중 해가 아니어서 막히면, 되돌아가서 다시 해를 찾아가는 기법을 말합니다.
# 최적화 문제와 결정 문제를 푸는 방법이 됩니다.

# 1 s = 1000 ms

# -필요한 부분-
# 응답 완료 시간에서 처리 시간을 빼서 시작 시간과 끝 시간의 범위를 구해줘야됨

lines = [
    "2016-09-15 01:00:04.002 2.0s",
    "2016-09-15 01:00:07.000 2s"
]


# 튜터님 풀이
# time은 로그의 처리 시작 시간 또는 처리 완료 시간
def get_request_count_during_one_second(time, start_and_end_times):
    request_count = 0
    start = time
    end = time + 1000
    for start_and_end_time in start_and_end_times:
        # start보다 로그의 종료시점이 크거나 같은 경우, end가 로그의 시작시점보다 큰 경우
        # => 1초 범위에 포함
        if start_and_end_time[1] >= start and start_and_end_time[0] < end:
            request_count += 1
    return request_count


def solution(lines):
    answer = 0
    start_and_end_times = []  # 각 로그의 처리 시작 시간과 종료 시간을 담는 리스트
    for line in lines:
        _, time, duration = line.split()
        time = time.split(':')
        duration = float(duration.replace('s', '')) * 1000  # 밀리세컨드로 변환
        end = (int(time[0]) * 3600 + int(time[1]) * 60 +
               float(time[2])) * 1000  # 종료 시간 전체를 밀리세컨드로 변환
        start = end - duration + 1
        start_and_end_times.append([start, end])

    for start_and_end_time in start_and_end_times:
        # 해당 로그의 처리 시작 시간, 처리 완료 시간을 get_request_count_during_one_second의 time 파라미터로
        # answer(최댓값)은 이전 answer, 현재 로그 처리 시작 시간부터 1초간 발생한 로그 개수, 현재 로그 처리 완료 시간부터 1초간 발생한 로그 개수 중 가장 큰 값
        answer = max(answer, get_request_count_during_one_second(start_and_end_time[0], start_and_end_times),
                     get_request_count_during_one_second(start_and_end_time[1], start_and_end_times))
    return answer


solution(lines)
