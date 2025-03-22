package BOJ.P2156_포도주_시식;

import java.util.*;
import java.io.*;

// DP
// 포도주 잔이 일렬로 놓여 있다
// 시식에는 2가지 규칙이 있다.
// 1. 포도주 잔을 선택하면 그 잔에 들어있는 포도주는 모두 마셔야 한다
// 마신 후에는 원래 위치에 다시 놓아야 한다.
// 2. 연속으로 놓여 있는 3잔을 모두 마실 수는 없다.
// 최대로 마실 수 있는 포도주의 양을 구하여라

public class Main {

    static int N;
    static int[] wine, dp;

    public static void main(String[] args ) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());

        wine = new int[N+1];
        dp = new int[N+1];

        for(int n = 1; n <= N; n++) {
            st = new StringTokenizer(br.readLine());
            wine[n] = Integer.parseInt(st.nextToken());
        }

        if(N==1) {
            System.out.println(wine[1]);
            return;
        } else if (N==2){
            System.out.println(wine[1] + wine[2]);
            return;
        }
        // dp[i] -> i번째 잔까지 있을 때의 최대 양

        dp[1] = wine[1];
        dp[2] = wine[1] + wine[2];

        for(int i = 3; i <= N; i++) {
            dp[i] = Math.max(dp[i-1], Math.max(dp[i-2] + wine[i], dp[i-3] + wine[i-1] +  wine[i]));
        }

        System.out.println(dp[N]);
    }
}