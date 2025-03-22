package BOJ.P2193_이친수;


import java.util.*;
import java.io.*;

// DP

// 이진수: 0과 1로 이루어진 수
// 이친수: 0으로 시작하지 않음, 1이 연속 2번 이상 나오지 않음
// N 자리의 이친수를 구하여라

public class Main {

    static int N;
    static long[] dp;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));


        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());


        if(N <= 2) {
            System.out.println(1);
            return;
        }

        dp = new long[N+1];

        dp[1] = 1;
        dp[2] = 1;

        for(int i = 3; i <=N; i++) {
            dp[i] = dp[i - 2] + dp[i - 1];
        }

        System.out.println(dp[N]);
    }

}
