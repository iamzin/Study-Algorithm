# 핵심은 musicnfos를 어떻게 파싱할것인가
# 파싱 3가지 필요
# 1. 시간 파싱
# 2. 음악 제목
# 3. 악보 정보

# 계산이 필요한 부분
# 1. 시간 -> 몇 분 동안 재생 되었는지 \제한 사항: 00:00을 넘겨서 재생되는 일은 없다.
# 2. 악보 정보 -> 시간 과 계산하여 재생된 악보 정보를 만들어야됨

m = "ABC"
musicinfos = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]

# 이걸 안하고 하려면 너무 복잡해짐


def sharp_change(string):
    string = string.replace("C#", "L").replace("D#", "M").replace(
        "F#", "N").replace("G#", "O").replace("A#", "P")
    return string


def solution(m, musicinfos):  # 정확성 절반 맞았음 -> # 이 들어가는 음계를 생각 못했음 => # 고려 했더니 정확성 76퍼 => replace로 해서 성공
    answer = []
    music_infos_parsed = []  # 파싱 리스트
    final_music_info_list = []  # [[제목,재생시간,음리스트], ...]
    m = sharp_change(m)
    for musicinfo in musicinfos:
        music_infos_parsed.append(list(map(str, musicinfo.split(','))))

    for music_info in music_infos_parsed:
        start_hour, start_min = map(int, music_info[0].split(":"))
        end_hour, end_min = map(int, music_info[1].split(":"))
        # 제한 사항: 00:00을 넘겨서 재생되는 일은 없다.
        if end_hour < start_hour and end_min >= 1:
            end_hour = 24
            end_min = 0
        time = 0
        # 재생 시간 계산
        if start_min < end_min:
            time = 60*(end_hour-1-start_hour) + \
                60+end_min-start_min
        else:
            time = 60*(end_hour-start_hour) + \
                end_min - start_min
        # 재생 시간 동안 나온 음 계산
        sharp_chageed_note = sharp_change(music_info[3])
        share, left = divmod(time, len(sharp_chageed_note))
        played_note = share * sharp_chageed_note + sharp_chageed_note[0:left+1]
        # 최종적으로 나온 정보 저장
        final_music_info_list.append([music_info[2], time, played_note])

    for i in range(0, len(final_music_info_list)):
        # temp = final_music_info_list[i][2].find(m)
        # print("temp: ", temp)
        # print("next: ", final_music_info_list[i][2][temp+len(m)])
        # if temp != -1 and len(final_music_info_list[i][2]) > temp+len(m) and final_music_info_list[i][2][temp+len(m)] != "#":
        #     answer.append(final_music_info_list[i])
        # # elif temp != -1 and len(final_music_info_list[i][2])-1 == temp+len(m):
        # #     answer.append(final_music_info_list[i])
        if m in final_music_info_list[i][2]:
            answer.append(final_music_info_list[i])
    if len(answer) != 0:
        answer.sort(key=lambda x: -x[1])
        return answer[0][0]
    else:
        return "(None)"


print(solution(m, musicinfos))
