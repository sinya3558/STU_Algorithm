package BOJ.P9465_스티커;

import java.util.*;
import java.io.*;

// DP
// 2n개의 스티커
// 2행 n열로 배치
// 스티커를 떼면 상, 하, 좌, 우 사용할 수 없게 됨
// 각 스티커에 점수를 부여 -> 점수의 합이 최대가 되도록 스티커를 떼어냄
// 2n개의 스티커 중 합이 최대이며, 서로 변을 공유하지 않는 스티커 집합을 구하라

public class Main {

    static int N;
    static long[][] sticker, dp;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int T = Integer.parseInt(st.nextToken());

        for(int test_case = 0; test_case < T; test_case++) {
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());

            sticker = new long[2][N+1];
            for(int i = 0; i < 2; i++) {
                st = new StringTokenizer(br.readLine());
                for(int j = 1; j <= N; j++) {
                    sticker[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            dp = new long[2][N+1];

            dp[0][1] = sticker[0][1];
            dp[1][1] = sticker[1][1];

            if(N == 1) {
                if(dp[0][1] > dp[1][1]) {
                    sb.append(dp[0][1]+"\n");
                } else {
                    sb.append(dp[1][1]+"\n");
                }
                continue;
            }

            for(int n = 2; n <= N; n++) {
                dp[0][n] = Math.max(dp[1][n-1] + sticker[0][n], dp[1][n-2] + sticker[0][n]);
                dp[1][n] = Math.max(dp[0][n-1] + sticker[1][n], dp[0][n-2] + sticker[1][n]);
            }

            sb.append(Math.max(dp[0][N], dp[1][N]) + "\n");
        }

        br.close();
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}

