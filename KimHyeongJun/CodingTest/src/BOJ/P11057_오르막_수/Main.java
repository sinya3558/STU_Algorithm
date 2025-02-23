package BOJ.P11057_오르막_수;

import java.util.*;
import java.io.*;

// 오르막수, 오름차순을 이루는 수
// 인접한 수가 같아도 오름차순
// 수의 길이 N이 주어졌을 때 오르막수의 개수를 구하라
// 수는 0으로 시작할 수 있다
// 예) N -> 2, 11, ..., 19, 22, .., 29, ..., 99
public class Main {

    static int N;
    static long[] dp, tmp;

    public static void main(String[] args) throws Exception {


        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        // dp[i] 앞자리가 i일때 오르막 수의 개수
        dp = new long[10];
        Arrays.fill(dp, 1);

        tmp = new long[10];
        Arrays.fill(tmp, 1);

        for(int n = 1; n < N; n++) {
            for(int i = 8; i >= 0; i--) {
                tmp[i] = (dp[i] + tmp[i+1]) % 10007;
            }

            dp = tmp.clone();
        }

        long answer = 0;
        for(long num : tmp) {
            answer = (answer + num) % 10007;
        }
        System.out.print(answer);
    }

}

