package BOJ.P1325_효율적인_해킹;

import java.util.*;
import java.io.*;

// N개의 컴퓨터로 이루어짐
// 한번의 해킹으로 여러 개의 컴퓨터를 해킹할 수 있는 컴퓨터를 해킹하려 함
// 컴퓨터는 신뢰 관계, 신뢰하지 않는 관계로 이루어짐
// A가 B를 신뢰 -> B를 해킹하면 A를 해킹할 수 있다
// 신뢰 관계가 주어졌을 때 한번에 가장 많은 해킹을 할 수 있는 컴퓨터 번호를 출력하라
// 번호는 오름차순으로 출력

public class Main {

    static int N, M;
    static List<Integer>[] topology;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());


        topology = new ArrayList[N+1];

        for(int n = 1; n <= N; n++) {
            topology[n] = new ArrayList<>();
        }

        int u, v;
        for(int m = 0; m < M; m++) {
            st = new StringTokenizer(br.readLine());
            u = Integer.parseInt(st.nextToken()); // 3
            v = Integer.parseInt(st.nextToken()); // 1
            topology[v].add(u);
        }

        int maxCount = 0;
        List<Integer> answer = new ArrayList<>();

        for(int n = 1; n <= N; n++) {
            if(topology[n].isEmpty()){
                continue;
            }


            Queue<Integer> queue = new LinkedList<>();
            queue.add(n);

            boolean[] visited = new boolean[N + 1];
            visited[n] = true;

            int tmp = 0;
            while(!queue.isEmpty()) {
                int node = queue.poll();
                for(int connectNode : topology[node]) {
                    if(visited[connectNode]) {
                        continue;
                    }

                    visited[connectNode] = true;
                    tmp += 1;

                    if(topology[connectNode].isEmpty()){
                        continue;
                    }

                    queue.add(connectNode);
                }
            }

            if(maxCount < tmp) {
                answer = new ArrayList<>();
                answer.add(n);
            } else if(maxCount == tmp) {
                answer.add(n);
            }
            maxCount = Math.max(tmp, maxCount);

        }

        Collections.sort(answer);

        for(int num : answer) {
            System.out.print(num + " ");
        }
    }
}
