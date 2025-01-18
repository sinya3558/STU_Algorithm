package BOJ.P15650_N과M_2;

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

        boolean[] used = new boolean[N+1];
        List<Integer> result = new ArrayList<>();

        BackTracking(used, result);

        br.close();
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }

    static void BackTracking(boolean[] used, List<Integer> result) {
        boolean[] tmpUsed = used.clone();
        if(result.size() == M) {
            for(Integer num : result) {
                sb.append(num + " ");
            }
            sb.append("\n");
            return;
        }

        for(int n = 1; n <= N; n++) {
            if(!tmpUsed[n]) {
                tmpUsed[n] = true;
                result.add(n);
                BackTracking(tmpUsed, result);
                result.remove(result.size() - 1);
            }
        }
    }
}
