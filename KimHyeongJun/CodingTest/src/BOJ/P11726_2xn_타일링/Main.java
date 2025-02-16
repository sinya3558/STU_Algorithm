package BOJ.P11726_2xn_타일링;

import java.util.*;
import java.io.*;

public class Main {

    static StringBuilder sb = new StringBuilder();
    static int[] dp;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        // n = 1 -> 1가지
        // n = 2 -> 2가지
        // n = 3 -> 3가지
        // n = 4 -> 5가지
        // n = (n - 1) + (n - 2)

        dp = new int[N + 1];
        dp[0] = 1;
        dp[1] = 1;

        for(int n = 2; n <= N; n++){
            dp[n] = (dp[n - 1] + dp[n - 2]) % 10007;
        }

        sb.append(dp[N]);

        br.close();
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }

}