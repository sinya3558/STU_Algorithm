package BOJ.P10844_쉬운_계단수;

import java.io.*;
import java.util.*;

// 계단 수 -> 인접한 모든 자리의 차이가 1
// 예) -> 45656

public class Main {

    static long[][] dp;
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));


        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());

        dp = new long[10][2];

        for(int i = 1; i < 10; i++){
            dp[i][1] = 1;
        }

        int MOD = 1000000000;
        if(N >= 2){
            for(int n = 2; n <= N; n++){
                long[][] tmp = new long[10][2];
                for(int i = 0; i < 10; i++) {
                    if(i == 0) {
                        tmp[1][1] += dp[0][1] % MOD;
                    } else if (i == 9){
                        tmp[8][1] += dp[9][1] % MOD;
                    } else {
                        tmp[i - 1][1] += dp[i][1] % MOD;
                        tmp[i + 1][1] += dp[i][1] % MOD;
                    }
                }
                dp = tmp;
            }
        }

        long answer = 0;
        for(int i = 0; i < 10; i++){
            answer += dp[i][1] % MOD;
        }

        sb.append(answer % MOD);

        br.close();
        bw.write(sb.toString());
        bw.flush();
        bw.close();

    }
}
