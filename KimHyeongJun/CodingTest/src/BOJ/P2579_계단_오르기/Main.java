package BOJ.P2579_계단_오르기;


import java.util.*;
import java.io.*;

// DP
//계단 오르는 데는 다음과 같은 규칙이 있다.

// 1. 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다.
// 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
// 2. 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
// 3. 마지막 도착 계단은 반드시 밟아야 한다.
// 따라서 첫 번째 계단을 밟고 이어 두 번째 계단이나, 세 번째 계단으로 오를 수 있다.
// 하지만, 첫 번째 계단을 밟고 이어 네 번째 계단으로 올라가거나, 첫 번째, 두 번째, 세 번째 계단을 연속해서 모두 밟을 수는 없다.

// 각 계단에 쓰여 있는 점수가 주어질 때 이 게임에서 얻을 수 있는 총 점수의 최댓값을 구하는 프로그램을 작성하시오.
public class Main {

    static int N;
    static int[] steps, dp;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        steps = new int[N + 1];


        for(int n = 1; n <= N; n++) {
            st = new StringTokenizer(br.readLine());
            steps[n] = Integer.parseInt(st.nextToken());
        }

        // 마지막 계단은 반드시 밟아야 한다

        if(N == 1) {
            System.out.println(steps[1]);
            return;
        } else if(N == 2) {
            System.out.println(steps[1] + steps[2]);
            return;
        }

        dp = new int[N + 1];
        dp[0] = 0;
        dp[1] = steps[1];
        dp[2] = steps[1] + steps[2];

        for(int n = 3; n <= N; n++) {
            dp[n] = Math.max(dp[n-2] + steps[n], dp[n-3] + steps[n-1] + steps[n]);
        }

        System.out.println(dp[N]);
    }
}

