package BOJ.P6118_숨바꼭질;

import java.util.*;
import java.io.*;

// 헛간들에 숨을려고 한다
// 헛간의 개수는 N(2 <= N <= 20,000)개이며, 1 부터 샌다.
// 모든 헛간은 M(1<= M <= 50,000)개의 양방향 길로 이어져 있다.
// 그 양 끝을 A_i 와 B_i(1<= A_i <= N; 1 <= B_i <= N; A_i != B_i)로 나타낸다.
// 또한 어떤 헛간에서 다른 헛간으로는 언제나 도달 가능하다고 생각해도 좋다.
// 1번 헛간부터 찾는다
// 1번 헛간에서 멀어질 수록 냄새가 감소함
// 1번 헛간에서 가장 먼 헛간이 무엇인지(가장 작은 번호)
// 1번 헛간과 해당 헛간까지의 거리
// 가장 먼 헛간의 수

class Node {
    int idx;
    int distance;

    Node(int idx, int distance){
        this.idx = idx;
        this.distance = distance;
    }
}


public class Main {

    static int N, M;
    static List<Integer>[] graph;
    static int maxDistance;
    static List<Integer> edgeNode;


    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

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

        Queue<Node> queue = new LinkedList<>();

        queue.add(new Node(1, 0));

        boolean[] visited = new boolean[N+1];
        visited[1] = true;

        int distance;
        maxDistance = Integer.MIN_VALUE;
        edgeNode = new ArrayList<>();

        while(!queue.isEmpty()) {
            Node node = queue.poll();
            distance = node.distance + 1;

            for(int nextNode : graph[node.idx]) {
                if(visited[nextNode]) {
                    continue;
                }

                visited[nextNode] = true;

                if(maxDistance < distance) {
                    edgeNode = new ArrayList<>();
                    edgeNode.add(nextNode);
                } else if (maxDistance == distance) {
                    edgeNode.add(nextNode);
                }

                maxDistance = Math.max(maxDistance, distance);
                queue.add(new Node(nextNode, distance));
            }
        }

        Collections.sort(edgeNode);
        System.out.println(edgeNode.get(0) + " " + maxDistance + " " + edgeNode.size());
    }
}
