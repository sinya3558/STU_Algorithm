package BOJ.P22871_징검다리_건너기_large;

import java.util.*;
import java.io.*;

// DP
// 가장 왼쪽에 있는 돌에서 가장 오른쪽에 있는 돌로 건너감

// 1. 항상 오른쪽으로만 이동할 수 있다.
// 2. i번째 돌에서 j(i < j)번째 돌로 이동할 때 (j - i) × (1 + |A_i - A_j|) 만큼 힘을 쓴다.
// 3. 돌을 한번 건너갈 때마다 쓸 수 있는 힘은 최대 K이다.
// 가장 왼쪽 돌에서 출발하여 가장 오른쪽에 있는 돌로 건너갈 수 있는 모든 경우 중 K 의 최솟값

public class Main {

    static int N;
    static long[] A;
    static long[] dp;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        A = new long[N+1];
        for(int n = 1; n <= N; n++) {
            A[n] = Long.parseLong(st.nextToken());
        }

        dp = new long[N+1];
        Arrays.fill(dp, Long.MAX_VALUE);
        dp[1] = 0;

        // 가장 왼쪽 돌과 가장 오른쪽 돌은 반드시 밟아야 한다.
        for(int j = 2; j <= N; j++) {
            for(int i = 1; i < j; i++) {
                long power = getPower(i, j);
                // 잘못된 코드
                // dp[j] 갱신을 잘못 하고있다.
                // 문제가 요구하는건 사용할 수 있는 힘의 최소 값이다.
                // i번째에서 오는 힘이 제일 작은 값을 찾는 것이 아니다.
//                if(power <= dp[j]) {
//                    dp[j] = Math.max(dp[i], power);
//                }

                dp[j] = Math.min(dp[j], Math.max(power, dp[i]));
            }
        }

        System.out.println(dp[N]);
    }

    static long getPower(int i, int j) {
        return (j - i) * (1 + Math.abs(A[i] - A[j]));
    }

}
