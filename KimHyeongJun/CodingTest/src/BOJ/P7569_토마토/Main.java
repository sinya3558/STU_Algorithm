package BOJ.P7569_토마토;

import java.util.*;
import java.io.*;


class Tomato {

    int z;
    int y;
    int x;
    int day;

    Tomato(int z, int y, int x, int day) {
        this.z = z;
        this.y = y;
        this.x = x;
        this.day = day;
    }

}


public class Main {
    // 위, 아래, 왼쪽, 오른쪽, 앞, 뒤
    static int[] dz = {-1, 1, 0, 0, 0, 0};
    static int[] dy = {0, 0, -1, 1, 0, 0};
    static int[] dx = {0, 0, 0, 0, -1 ,1};

    static int M, N, H;
    static int[][][] box;
    static int[][][] visited;
    static int targetTomato;
    static int answer;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());

        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        H = Integer.parseInt(st.nextToken());

        Queue<Tomato> queue = new LinkedList<>();

        box = new int[H][N][M];
        visited = new int[H][N][M];
        targetTomato = 0;
        for(int h = 0; h < H; h++){
            for(int n = 0; n < N; n++){
                st = new StringTokenizer(br.readLine());
                for(int m = 0; m < M; m++){
                    int tmp = Integer.parseInt(st.nextToken());
                    if(tmp == 1) {
                        queue.add(new Tomato(h, n, m, 0));
                        visited[h][n][m] = 1;
                    } else if (tmp == 0) {
                        targetTomato += 1;
                    }
                    box[h][n][m] = tmp;

                }
            }
        }

        answer = 0;

        if(targetTomato == 0){
            sb.append(answer);
        } else {
            BFS(queue);
            if(targetTomato == 0){
                sb.append(answer);
            } else {
                sb.append(-1);
            }
        }

        br.close();
        bw.write(sb.toString());
        bw.flush();
        bw.close();

    }


    static void BFS(Queue<Tomato> queue) {
        while(!queue.isEmpty()) {
            // 1. 큐에서 꺼낸다.
            Tomato tomato = queue.poll();

            int z = tomato.z;
            int y = tomato.y;
            int x = tomato.x;
            int day = tomato.day;
            // 2. 목적지인가
            // 3. 연결된 곳 순회
            for(int i = 0; i < 6; i++) {
                int tz = z + dz[i];
                int ty = y + dy[i];
                int tx = x + dx[i];

                // 4. 갈 수 있는가
                if(tz < 0 || tz >= H || ty < 0 || ty >= N || tx < 0 || tx >= M) {
                    continue;
                }

                if(box[tz][ty][tx] == 0 && visited[tz][ty][tx] == 0) {
                    // 5. 체크인
                    visited[tz][ty][tx] = 1;
                    // 6. 큐에 넣는다

                    queue.add(new Tomato(tz, ty, tx, day + 1));
                    targetTomato -= 1;
                    answer = day + 1;
                }
            }
            // 7. 체크아웃
        }
    }
}
