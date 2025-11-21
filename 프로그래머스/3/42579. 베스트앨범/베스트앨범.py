from collections import deque

def solution(genres, plays):
    answer = []
    
    # 정보 구조화
    songs = [(idx, genre, play) for idx, (genre, play) in enumerate(zip(genres,plays))]

    # 같은 장르끼리 총 재생수 저장
    genre_sum={}
    for genre, play in zip(genres, plays):
        genre_sum[genre]=genre_sum.get(genre,0)+play
    
    # 인기 많은 장르순 정렬
    genre_sum=sorted(genre_sum.items(), key=lambda x:x[1], reverse=True)
    
    # 각 장르 안에서 재생수 상위 2개 선택
    genre_dict={}
    for i,g,p in songs:
        genre_dict.setdefault(g,[]).append((p,i))
    
    for g in genre_dict:
        genre_dict[g].sort(key=lambda x:(-x[0], x[1]))
    
    # 정렬된 순서대로 결과 추출
    for g,_ in genre_sum:
        top_two=genre_dict[g][:2]
        for _,i in top_two:
            answer.append(i)
    return answer