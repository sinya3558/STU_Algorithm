package BOJ.P1012_유기농_배추;

import java.util.*;
import java.io.*;

class Cabbage {
    int y;
    int x;

    Cabbage(int y, int x){
        this.y = y;
        this.x = x;
    }
}

// 상, 하, 좌, 우
public class Main {

    // M: 가로 길치
    // N: 세로 길이
    // K: 배추의 수
    static int M, N, K;
    static int[][] land;

    // 상, 하, 좌, 우
    static int[] dy = {-1, 1 ,0, 0};
    static int[] dx = {0, 0, -1, 1};
    static boolean[][] visited;

    static int answer;
    static StringBuilder sb;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int T = Integer.parseInt(st.nextToken());

        sb = new StringBuilder();
        for(int test_case = 0; test_case < T; test_case++) {
            st = new StringTokenizer(br.readLine());
            M = Integer.parseInt(st.nextToken());
            N = Integer.parseInt(st.nextToken());
            K = Integer.parseInt(st.nextToken());

            land = new int[N][M];

            for(int k = 0; k < K; k++) {
                st = new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());

                land[y][x] = 1;
            }


            visited = new boolean[N][M];
            answer = 0;
            for(int n = 0; n < N; n++) {
                for(int m = 0; m < M; m++) {
                    if(land[n][m] == 1 && !visited[n][m]) {

                        visited[n][m] = true;
                        BFS(n, m);
                        answer += 1;
                    }
                }
            }

            sb.append(String.valueOf(answer) + "\n");

        }
        br.close();
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }

    static void BFS(int n, int m) {
        Queue<Cabbage> queue = new LinkedList<>();

        queue.add(new Cabbage(n, m));

        while(!queue.isEmpty()) {
            Cabbage cabbage = queue.poll();
            for(int i = 0; i < 4; i++) {
                int ty = cabbage.y + dy[i];
                int tx = cabbage.x + dx[i];

                if(ty <= -1 || ty >= N || tx <= -1 || tx >= M) {
                    continue;
                }

                if(land[ty][tx] == 0 || visited[ty][tx]) {
                    continue;
                }

                visited[ty][tx] = true;
                queue.add(new Cabbage(ty, tx));
            }
        }
    }
}
