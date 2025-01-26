package SWA.P2382_미생물_격리;

import java.util.*;
import java.io.*;

// 1. 미생물 배치
// 1-1. 약품이 칠해진 부분에는 배치 X, 이동 방향은 상, 하, 좌, 우 중 하나
// 2. 1식나 마다 이동 방향에 있는 다음 셀로 이동
// 3. 약품 도착 -> 절반, 방향 반대, 홀수 -> 소수점 버림, 0 -> 군집이 사라짐
// 4. 이동 후 -> 한 셀에 있는 경우 합쳐짐 -> 방향은 가장 많은 군집의 방향, 같은 경우는 없다


class Cluster {
    int y;
    int x;
    int dir;
    long num;
    int day;

    Cluster(int y, int x, int dir, long num, int day) {
        this.y = y;
        this.x = x;
        this.dir = dir;
        this.num = num;
        this.day = day;
    }
}


public class Solution {

    // N: 한 변의 셀의 수
    // M: 격리 시간
    // K: 군집 수
    static int N, M, K;
    static Map<String, List<Cluster>> cells;

    static int[] dy = {0, -1, 1, 0, 0};
    static int[] dx = {0, 0, 0, -1, 1};

    static long answer;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int T = Integer.parseInt(st.nextToken());

        for(int test_case = 1; test_case <= T; test_case++) {
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());
            K = Integer.parseInt(st.nextToken());

            // 약품에는 미생물 배치 X
            // dir -> 상: 1, 하: 2, 좌: 3, 우: 4

            cells = new HashMap<>();

            Queue<Cluster> queue = new LinkedList<>();
            answer = 0;
            for(int k = 0; k < K; k++) {
                st = new StringTokenizer(br.readLine());
                int y = Integer.parseInt(st.nextToken());
                int x = Integer.parseInt(st.nextToken());
                long num = Long.parseLong(st.nextToken());
                int dir = Integer.parseInt(st.nextToken());

                answer += num;
                Cluster cluster = new Cluster(y, x, dir, num, 0);
                List<Cluster> tmp = new ArrayList<>();
                tmp.add(cluster);
                cells.put(y+","+x, tmp);
                queue.add(cluster);
            }

            BFS(queue);

            sb.append("#"+test_case+" "+answer+"\n");

        }

        br.close();
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
    static void BFS(Queue<Cluster> queue) {
        while(true) {
            Cluster cluster = queue.poll();

            int y = cluster.y;
            int x = cluster.x;
            int dir = cluster.dir;
            long num = cluster.num;
            int day = cluster.day;

            int ty = y + dy[dir];
            int tx = x + dx[dir];

            if(ty == 0 || ty == N - 1 || tx == 0 || tx == N - 1) {
                answer -= num;
                num /= 2;
                answer += num;
                dir = reverseDir(dir);
            }

            day += 1;
            cells.get(y+","+x).remove(cluster);

            cluster.y = ty;
            cluster.x = tx;
            cluster.dir = dir;
            cluster.num = num;
            cluster.day = day;
            if(cells.get(ty+","+tx) == null) {
                cells.put(ty+","+tx, new ArrayList<>());
            }
            cells.get(ty+","+tx).add(cluster);

            // queue.isEmpty() -> 이동을 완료 하였는가
            if(queue.isEmpty()) {
                if(day == M) {
                    return;
                }
                queue = mergeCluster();
            }
        }
    }

    static int reverseDir(int dir) {
        if(dir == 1) {
            return 2;
        } else if(dir == 2) {
            return 1;
        } else if(dir == 3) {
            return 4;
        } else {
            return 3;
        }
    }

    static Queue<Cluster> mergeCluster() {
        Map<String, List<Cluster>> newCells = new HashMap<>();
        Queue<Cluster> queue = new LinkedList<>();

        for(String key : cells.keySet()) {
            List<Cluster> clusterList = cells.get(key);
            if(clusterList == null || clusterList.isEmpty()){
                continue;
            }

            Cluster newCluster = clusterList.get(0);

            // 같은 cell에서 가장 많은 군집의 수
            long maxNum = newCluster.num;

            for(int i = 1; i < clusterList.size(); i++) {
                if(maxNum < clusterList.get(i).num) {
                    maxNum = clusterList.get(i).num;
                    newCluster.dir = clusterList.get(i).dir;
                }

                newCluster.num += clusterList.get(i).num;
            }
            List<Cluster> tmp = new ArrayList<>();
            tmp.add(newCluster);
            newCells.put(newCluster.y+","+ newCluster.x, tmp);
            queue.add(newCluster);
        }
        cells = newCells;
        return queue;
    }
}
