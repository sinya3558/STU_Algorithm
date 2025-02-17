package BOJ.P14712_넴모넴모_Easy;

import java.util.*;
import java.io.*;

// 나올 수 없는 모든 가지 수
// "넴모"로 구성할 수 있는 모든 가지 수 - "넴모"를 모두 없앨 수 있는 경우의 수
// 2^(N*M) - "넴모"를 모두 없앨 수 있는 경우의 수
// N*M board에 2x2를 채울 수 있는 경우의 수는 몇가지인가?

class Main {

    static int N, M;
    static boolean[][] visited;
    static int answer;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        visited = new boolean[N+1][M+1];
        answer = 0;
        DFS(0);
        System.out.println(answer);
    }

    static void DFS(int depth) {
        if(depth == N * M){
            answer++;
            return;
        }

        // 0부터 N*M-1까지의 인덱스를 기준으로 행과 열 좌표 구하기
        int n = depth / M + 1;
        int m = depth % M + 1;

        if(visited[n-1][m] && visited[n][m-1] && visited[n-1][m-1]){
            DFS(depth + 1);
        } else {
            visited[n][m] = true;
            DFS(depth + 1);
            visited[n][m] = false;
            DFS(depth + 1);

        }
    }
}