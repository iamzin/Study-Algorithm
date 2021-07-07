
def solution(m, musicinfos):
    answer=[]
    m=m.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
    
    for i in range(len(musicinfos)):
        musicinfo=musicinfos[i]
        info=musicinfo.split(',')
        st, et, title, melody=info

        sh, sm= st.split(':')
        eh, em= et.split(':')

        play_time=(int(eh)-int(sh))*60+(int(em)-int(sm))

        melody=melody.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')

        melody=melody*(play_time//len(melody))+melody[0:play_time%len(melody)]
        if m in melody:
            answer.append((play_time,title))


    
    print(answer)
    answer.sort(key= lambda x: -x[0]) 

    if answer:
        return answer[0][1]

    else: 
        return "(None)"
    

    
    



solution("ABC",["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"])