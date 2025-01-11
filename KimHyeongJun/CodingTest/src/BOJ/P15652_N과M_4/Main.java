package BOJ.P15652_N과M_4;

import java.util.*;
import java.io.*;

public class Main {

    static int N, M;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        List<Integer> result = new ArrayList<>();

        BackTracking(result, 1, 0);

        br.close();
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }

    static void BackTracking(List<Integer> result, int start, int depth) {
        if(depth == M) {
            for(Integer num : result) {
                sb.append(num + " ");
            }
            sb.append("\n");
            return ;
        }

        for(int n = start; n <= N; n++) {
            result.add(n);
            BackTracking(result, n, depth + 1);
            result.remove(result.size() - 1);
        }
    }
}