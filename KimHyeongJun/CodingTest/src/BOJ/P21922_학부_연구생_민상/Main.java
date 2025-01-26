package BOJ.P21922_학부_연구생_민상;

import java.util.*;
import java.io.*;

class Wind {
    int y;
    int x;

    // 바람 방향
    // 좌, 우, 위, 아래
    int dir;

    Wind(int y, int x, int dir){
        this.y = y;
        this.x = x;
        this.dir = dir;
    }

}

public class Main {


    // 세로 N, 가로 M
    static int N, M;

    static int[][] lab;
    static int[][] visited;

    // 상, 하, 좌, 우
    static int[] dy = {0, -1, 1, 0, 0};
    static int[] dx = {0, 0, 0, -1 ,1};

    static int answer;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        lab = new int [N][M];
        visited = new int[N][M];
        Queue<Wind> queue = new LinkedList<>();
        answer = 0;

        for(int n = 0; n < N; n++) {
            st = new StringTokenizer(br.readLine());
            for(int m = 0; m < M; m++){
                int tmp = Integer.parseInt(st.nextToken());
                lab[n][m] = tmp;

                if(tmp == 9){
                    queue.add(new Wind(n, m, 1));
                    queue.add(new Wind(n, m, 2));
                    queue.add(new Wind(n, m, 3));
                    queue.add(new Wind(n, m, 4));
                    visited[n][m] = 1;
                    answer += 1;
                }
            }
        }

        // 물건을 기준으로 바람이 어느 방향으로 불어 오느냐를 봐야 한다.
        // BFS를 활용해보자.

        BFS(queue);

        br.close();
        bw.write(String.valueOf(answer));
        bw.flush();
        bw.close();
    }

    static void BFS(Queue<Wind> queue) {

        while(!queue.isEmpty()) {
            Wind wind = queue.poll();

            int y = wind.y;
            int x = wind.x;
            int dir = wind.dir;

            int ty = y + dy[dir];
            int tx = x + dx[dir];

            addQueue(queue, ty, tx, dir);

        }
    }

    static boolean dirCheck(int ty, int tx) {
        if(ty < 0 || ty >= N || tx < 0 || tx >= M) {
            return false;
        }
        return true;
    }

    static void addQueue(Queue<Wind> queue, int ty, int tx, int dir) {

        if(!dirCheck(ty, tx)){
            return;
        }

        if(lab[ty][tx] == 9) {
            return;
        }

        if(visited[ty][tx] == 0){
            visited[ty][tx] = 1;
            answer += 1;
        }

        if(lab[ty][tx] == 1) {
            if(dir == 3) {
                return ;
            } else if (dir == 4){
                return ;
            }
        }

        else if(lab[ty][tx] == 2) {
            if(dir == 1) {
                return ;
            } else if (dir == 2){
                return ;
            }
        }

        else if(lab[ty][tx] == 3) {
            if(dir == 1) {
                dir = 4;
            } else if (dir == 2){
                dir = 3;
            } else if (dir == 3){
                dir = 2;
            } else if (dir == 4){
                dir = 1;
            }
        }
        else if(lab[ty][tx] == 4) {
            if(dir == 1) {
                dir = 3;
            } else if (dir == 2){
                dir = 4;
            } else if (dir == 3){
                dir = 1;
            } else if (dir == 4){
                dir = 2;
            }
        }
        queue.add(new Wind(ty, tx, dir));

    }
}
