
def solution(m, musicinfos):

    #정답 후보 리스트
    answer=[]
    m=m.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
    
    for i in range(len(musicinfos)):
        musicinfo=musicinfos[i]
        info=musicinfo.split(',')
        st, et, title, melody=info

        sh, sm= st.split(':')
        eh, em= et.split(':')

        #재생시간
        play_time=(int(eh)-int(sh))*60+(int(em)-int(sm))

        #'#' 변환
        melody=melody.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
        #재싱시간 동안 이어지는 멜로디
        melody=melody*(play_time//len(melody))+melody[0:play_time%len(melody)]

        #m이 멜로디에 있으면 정답 후보에 넣는다.
        if m in melody:
            answer.append((play_time,title))

    #재생시간이 긴 음악을 우선으로 한다.
    #재생시간이 같을 경우의 우선순위는 먼저 입력된 음악이지만, musicinfos를 조회하면서 입력된 음악 순서대로 정답후보 리스트에 넣었기 때문에 따로 정렬하지 않는다.
    answer.sort(key= lambda x: -x[0]) 

    if answer:
        return answer[0][1]

    else: 
        return "(None)"
    

    
    



solution("ABC",["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"])