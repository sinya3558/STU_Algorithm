package BOJ.P1389_케빈_케이번의_6단계_법칙;

import java.util.*;
import java.io.*;

// 케빈 베이컨의 6단계 법칙
// 지구의 모든 사람은 최대 6단계 이내 서로 아는 사람으로 연결될 수 있따.
// 케빈 베이컨 게임
// 임의의 두 사람이 최소 몇 단계 만에 이어질 수 있는지 계산

// 천민호 이강호
// 천민호 최백준
// 최백준 김선영
// 김선영 김도현
// 김도현 민세희
// 케빈 베이컨 수: 본인 기준 모든 노드까지 거리의 합
// 케빈 베이컨 수가 가장 작은 사람을 구하여라
// 여러명일 경우 번호가 가장 작은 사람을 출력

class Friend {
    int idx;
    int distance;

    Friend(int idx, int distance){
        this.idx = idx;
        this.distance = distance;
    }
}

class Main {

    static int N, M;
    static List<Integer>[] graph;
    static int minKavinBacon;
    static List<Integer> result;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        graph = new ArrayList[N+1];
        for(int n = 1; n <= N; n++) {
            graph[n] = new ArrayList<>();
        }

        int u, v;
        for(int m = 0; m < M; m++) {
            st = new StringTokenizer(br.readLine());

            u = Integer.parseInt(st.nextToken());
            v = Integer.parseInt(st.nextToken());
            graph[u].add(v);
            graph[v].add(u);
        }

        Queue<Friend> queue;

        minKavinBacon = Integer.MAX_VALUE;
        int tmpKavinBacon = 0;
        result = new ArrayList<>();
        for(int n = 1; n <= N; n++) {
            queue = new LinkedList<>();
            queue.add(new Friend(n, 0));
            boolean[] visited = new boolean[N+1];
            visited[n] = true;
            int distance;
            while(!queue.isEmpty()) {
                Friend friend = queue.poll();

                distance = friend.distance + 1;

                for(int node : graph[friend.idx]) {
                    if(visited[node]) {
                        continue;
                    }
                    visited[node] = true;
                    tmpKavinBacon += distance;
                    queue.add(new Friend(node, distance));
                }
            }
            if(minKavinBacon > tmpKavinBacon) {
                result = new ArrayList<>();
                result.add(n);
            } else if (minKavinBacon > tmpKavinBacon){
                result.add(n);
            }
            minKavinBacon = Math.min(minKavinBacon, tmpKavinBacon);
            tmpKavinBacon = 0;
        }

        Collections.sort(result);

        System.out.println(result.get(0));
    }
}
