# 방금 그곡 - 구현 - 17683
'''
라디오를 자주 듣는 네오는 라디오에서 방금 나왔던 음악이 무슨 음악인지 궁금해질 때가 많다. 
그럴 때 네오는 다음 포털의 '방금그곡' 서비스를 이용하곤 한다. 
방금그곡에서는 TV, 라디오 등에서 나온 음악에 관해 제목 등의 정보를 제공하는 서비스이다.

네오는 기억한 멜로디를 재생 시간과 제공된 악보를 직접 보면서 비교하려고 한다. 다음과 같은 가정을 할 때 네오가 찾으려는 음악의 제목을 구하여라.


방금그곡 서비스에서는 음악 제목, 재생이 시작되고 끝난 시각, 악보를 제공한다.
네오가 기억한 멜로디와 악보에 사용되는 음은 C, C#, D, D#, E, F, F#, G, G#, A, A#, B 12개이다.
각 음은 1분에 1개씩 재생된다. 음악은 반드시 처음부터 재생되며 음악 길이보다 재생된 시간이 길 때는 음악이 끊김 없이 처음부터 반복해서 재생된다. 음악 길이보다 재생된 시간이 짧을 때는 처음부터 재생 시간만큼만 재생된다.
음악이 00:00를 넘겨서까지 재생되는 일은 없다.
조건이 일치하는 음악이 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다. 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환한다.
조건이 일치하는 음악이 없을 때에는 “(None)”을 반환한다.
'''
import datetime


def solution(m, musicinfos):
    # musicinfos에서 재생시간을 구한다......
    times = [(datetime.datetime.strptime(i.split(
        ',')[1], '%H:%M') - datetime.datetime.strptime(i.split(',')[0], '%H:%M')).seconds//60 for i in musicinfos]

    # print(times)

    # melody를 재생시간만큼 반복시켜 구한다..
    melodys = []
    for i, musicinfo in enumerate(musicinfos):
        music = musicinfo.split(',')[-1]
        # print(shop_count)
        music *= (times[i])  # 범위 실수 했었음
        # print(music)
        shop_count = music[:times[i]+1].count('#')
        # print(shop_count)
        melody = ''
        for j in range(times[i]+shop_count):
            melody += music[j]
        melodys.append(melody)
    # print(melodys)

    # C# 같은애들 소문자로 치환..
    new_melodys = []
    for melody in melodys:
        if 'C#' in melody:
            melody = melody.replace('C#', 'c')
            new_melodys.append(melody)
        elif 'D#' in melody:
            melody = melody.replace('D#', 'd')
            new_melodys.append(melody)
        elif 'F#' in melody:
            melody = melody.replace('F#', 'f')
            new_melodys.append(melody)
        elif 'G#' in melody:
            melody = melody.replace('G#', 'g')
            new_melodys.append(melody)
        elif 'A#' in melody:
            melody = melody.replace('A#', 'a')
            new_melodys.append(melody)
        else:
            new_melodys.append(melody)
    # print(new_melodys)

    if 'C#' in m:
        m = m.replace('C#', 'c')
    elif 'D#' in m:
        m = m.replace('D#', 'd')
    elif 'F#' in m:
        m = m.replace('F#', 'f')
    elif 'G#' in m:
        m = m.replace('G#', 'g')
    elif 'A#' in m:
        m = m.replace('A#', 'a')

    # print(new_melodys)
    # print(m)

    temp = []
    for i in range(len(new_melodys)):
        # 주어진 음이 멜로디들 안에 포함되어 있으면 인덱스를 저장인데
        if m in new_melodys[i]:
            temp.append(i)
    if temp == []:
        return "(None)"

    # 같은 멜로디가 포함된 노래가 있을경우 - 재생시간이 긴 것을 출력하라고 했다. 그래서 위에서 인덱스 저장
    max_len_music = 0  # 재생시간이 제일 긴 노래
    for t in temp:
        if max_len_music <= times[t]:
            max_len_music = times[t]

    # 그노래의 인덱스
    idx = times.index(max_len_music)
    # 답안 도출

    return musicinfos[idx].split(',')[2]


# print(
#     solution('ABCDEFG', ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
# print(solution('CC#BCC#BCC#BCC#B', [
#       "03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(
    solution('ABC#', ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
# print(
#     solution('ABC#', ["12:15,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
