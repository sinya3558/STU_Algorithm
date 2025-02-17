package BOJ.P2606_바이러스;

import java.util.*;
import java.io.*;


// 한 컴퓨터가 바이러스에 걸리면 그 컴퓨터와 네트워크 상에 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸린다.
// 1번 컴퓨터가 바이러스에 걸렸다. -> 1번을 통해 바이러스에 감염되는 컴퓨터의 수는 몇개인가?

// N: 컴퓨터의 수(노드의 수)
// 직접 연결되어 있는 컴퓨터 쌍의 수(간선의 수)

public class Main {

    static int N, E;
    static List<Integer>[] topology;
    static int answer;
    static boolean[] visited;
    static Queue<Integer> queue;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        E = Integer.parseInt(st.nextToken());

        topology = new ArrayList[N + 1];

        for(int n = 1; n <= N; n++) {
            topology[n] = new ArrayList<>();
        }


        for(int e = 0; e < E; e++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());

            topology[u].add(v);
            topology[v].add(u);
        }

        visited = new boolean[N+1];
        queue = new LinkedList<>();

        visited[1] = true;
        queue.add(1);
        answer = 0;

        BFS();
        System.out.println(answer);
    }

    static void BFS(){
        while(!queue.isEmpty()) {
            int node = queue.poll();
            for(Integer nearNode : topology[node]) {

                if(visited[nearNode]){
                    continue;
                }

                visited[nearNode] = true;
                queue.add(nearNode);
                answer+=1;
            }
        }
    }
}
