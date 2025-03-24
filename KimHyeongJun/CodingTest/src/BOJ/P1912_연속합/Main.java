package BOJ.P1912_연속합;


import java.util.*;
import java.io.*;


// DP
// n 개의 정수로 이루어진 임의 수열
// 연속된 몇개의 수를 선택 -> 가장 큰 합
// 단, 1개 이상 선택


public class Main {

    static int N;
    static int[] nums, dp;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());

        nums = new int[N+1];
        st = new StringTokenizer(br.readLine());
        for(int n = 1; n <= N; n++) {
            nums[n] = Integer.parseInt(st.nextToken());
        }

        if(N == 1) {
            System.out.println(nums[1]);
            return;
        }

        dp = new int[N+1];
        dp[1] = nums[1];
        int answer = nums[1];
        for(int n = 2; n <= N; n++) {
            dp[n] = Math.max(dp[n - 1] + nums[n], nums[n]);
            answer = Math.max(answer, dp[n]);
        }
        System.out.println(answer);
    }
}
