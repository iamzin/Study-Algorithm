def solution(genres, plays):
    answer = []
    length= len(genres)
    genre_dict={} 
    song_dict={} 


    for i in range(length): 
        genre=genres[i]
        play= plays[i]
        if genre in genre_dict:
            genre_dict[genre]+=play
        else:
            genre_dict[genre]=play

        if genre in song_dict:
            song_dict[genre].append((i, play))
        else: 
            song_dict[genre]=[(i,play)]

    for key,value in sorted(genre_dict.items(), key=lambda item: item[1],reverse=True):
        
        #정렬 다중 조건 기억하기!
        cnt= 0
        for  id, play in sorted(song_dict[key], key=lambda song: (-song[1], song[0])):
            answer.append(id)
            cnt+=1
            if(cnt==2): 
                break

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))