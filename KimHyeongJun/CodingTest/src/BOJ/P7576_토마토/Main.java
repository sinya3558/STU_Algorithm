package BOJ.P7576_토마토;

import java.io.*;
import java.util.*;

class Tomato {
    int y;
    int x;
    int day;

    Tomato(int y, int x, int day){
        this.y = y;
        this.x = x;
        this.day = day;
    }

}

public class Main {

    static int M, N;
    static int[][] box;
    static int[][] visited;
    static StringBuilder sb = new StringBuilder();
    static int targetTomato;
    static int answer = Integer.MIN_VALUE;


    // 상, 하, 좌, 우
    static int[] dy = {-1, 1, 0, 0};
    static int[] dx = {0, 0, -1, 1};


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());

        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());

        box = new int[N][M];
        visited = new int[N][M];
        targetTomato = 0;

        Queue<Tomato> queue = new LinkedList<>();

        for(int n = 0; n < N; n++){
            st = new StringTokenizer(br.readLine());
            for(int m = 0; m < M; m++){
                int tmp = Integer.parseInt(st.nextToken());
                if(tmp == 1) {
                    queue.add(new Tomato(n, m, 0));
                    visited[n][m] = 1;
                } else if(tmp == 0){
                    targetTomato += 1;
                }
                box[n][m] = tmp;
            }
        }


        if(targetTomato == 0){
            sb.append(0);
        } else {
            bfs(queue);

            if(targetTomato == 0){
                sb.append(answer);
            } else if(targetTomato != 0){
                sb.append(-1);
            }
        }

        br.close();
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }

    static void bfs(Queue<Tomato> queue){

        while(!queue.isEmpty()) {
            // 1. 큐에서 꺼내온다.
            Tomato tomato = queue.poll();

            // 2. 목적지인가
            // 3. 연결된 곳 순회
            int my = tomato.y;
            int mx = tomato.x;
            int day = tomato.day;

            for(int i = 0; i < 4; i++) {
                int ty = my + dy[i];
                int tx = mx + dx[i];

                // 4. 갈 수 있는가
                if(ty < 0 || ty >= N || tx < 0 || tx >= M) {
                    continue;
                }

                if(box[ty][tx] == 0 && visited[ty][tx] == 0) {
                    // 5. 체크인
                    visited[ty][tx] = 1;

                    // 6. 큐에 넣는다.
                    queue.add(new Tomato(ty, tx, day + 1));
                    answer = day + 1;
                    targetTomato -= 1;
                }
            }

            // 7. 체크아웃
        }
    }
}
