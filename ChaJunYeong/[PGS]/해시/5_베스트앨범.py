def solution(genres, plays):
    
    """
        00:14:32.18

        장르 별 가장 많이 재생된 노래를 두 개 씩 모아 베스트 앨범 출시
        조건 1 : 속한 노래가 가장 많이 재생된 장르 먼저 수록
        조건 2 : 장르 내에서 많이 재생된 노래 먼저 수록
        조건 3 : 장르 내 재생 횟수가 같다면 고유 번호가 낮은 노래 먼저 수록

        풀이 :
            장르 별 재생 횟수 hash map과 음악 정보 (곡 별 재생횟수 및 고유 번호) hash map 저장
                1. 장르 별 전체 재생 횟수 기준으로 내림 차순 정렬
                2. 곡 별 재생 횟수 기준으로 내림 차순 정렬
                3. 동일할 경우, 고유번호 기준으로 오름차순 정렬
                4. 최대 2개의 곡 수록
    """

    music_info = {genre: [] for genre in genres}
    play_counts = {genre: 0 for genre in genres}

    for i in range(len(genres)):
        music_info[genres[i]].append((plays[i], i))
        play_counts[genres[i]] += plays[i]

    # 1. 장르 별 전체 재생 횟수 기준으로 내림차순 정렬
    play_counts = sorted(play_counts.items(), key=lambda x: x[-1], reverse=True)

    answer = []
    for genre, _ in play_counts:
        musics = music_info[genre]

        # 2. 곡 별 재생 횟수 기준으로 내림차순 정렬
        # 3. 동일할 경우, 고유번호 기준 오름차순 정렬
        musics.sort(key=lambda x: (-x[0], x[1]))

        # 4. 최대 2개의 곡 수록
        for music in musics[:2]:
            answer.append(music[1])
    return answer


def main():
    print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))


if __name__ == "__main__":
    main()
