package Tmp.P12865;

import java.util.*;
import java.io.*;

// DP
// 배낭을 가치있게 싸려 함
// 여행에 필요한 물건 N개
// W: 무게, V: 가치
// 배낭에 K 무게 만큼 넣을 수 있음, 배낭에 넣을 수 있는 가치의 최댓값은?


public class Main {

    static int N, K;
    static int[] weights, values, dp;
    static int answer;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        weights = new int[N];
        values = new int[N];
        for(int n = 0; n < N; n++) {
            st = new StringTokenizer(br.readLine());
            weights[n] = Integer.parseInt(st.nextToken());
            values[n] = Integer.parseInt(st.nextToken());
        }

        dp = new int[K+1];

        answer = 0;
        for(int n = 0; n < N; n++) {
            for(int k = K; k >= weights[n]; k--) {
                dp[k] = Math.max(dp[k], dp[k - weights[n]] + values[n]);
            }
            answer = Math.max(answer, dp[K]);
        }
        sb.append(String.valueOf(answer));

        br.close();
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}
