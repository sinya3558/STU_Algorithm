package BOJ.P15651_N과_M_3;

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
        BackTracking(result, 0);

        br.close();
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }

    static void BackTracking(List<Integer> result, int depth) {
        if(depth == M) {
            for(int num : result) {
                sb.append(num + " ");
            }
            sb.append("\n");
            return;
        }

        for(int n = 1; n <= N; n++) {
            result.add(n);
            BackTracking(result, depth + 1);
            result.remove(result.size() - 1);
        }
    }
}
