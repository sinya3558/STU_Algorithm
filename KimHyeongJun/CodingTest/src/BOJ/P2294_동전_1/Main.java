package BOJ.P2294_동전_1;

import java.util.*;
import java.io.*;

// n가지 종류의 동전
// 그 가치의 합이 kr가 되게 하고 싶다
// 동전의 수는 최소가 되었으면 좋겠다.
// 각각의 동전은 몇개라도 활용 가능
// 사용한 동전의 최소 개수를 출력
public class Main {

    static int N, K;
    static int[] values, dp;


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        values = new int[N+1];
        for(int n = 1; n <= N; n++) {
            st = new StringTokenizer(br.readLine());
            int tmp = Integer.parseInt(st.nextToken());
            // k의 범위는 1 <= K <= 10,000
            // 동전의 가치는 100,000보다 작거나 같다.
            // 그러므로 k보다 큰 값은 저장하지 않는다.
            if(tmp > K) {
                continue;
            }
            values[n] = tmp;
        }

        // dp[i] = i원을 만들기 위한 동전의 개수
        dp = new int[K+1];

        // 처음에 Integer.MAX_VALUE로 채웠으나, 이는 오버플로우가 발생할 수 있다.
        // k의 범위는 1 <= K <= 10,000이기 때문에 최대로 가질 수 있는 값은 1원으로 10,000개를 채웠을 때이다.
        // 그래서 1원 10,000개로도 만들 수 없는 10,001로 채워준다.
        Arrays.fill(dp, 10001);
        dp[0] = 0;

        for(int value : values) {
            for (int i = value; i <= K; i++) {
                // 원래 i원을 만들 때 필요한 동전의 수
                // i - value 원을 만들 때 필요한 동전의 수 + 1(value원 코인 1개)
                // 위 둘을 비교하더 더 작은 것을 i원을 만들 때 필요한 동전의 수로 저장한다.
                dp[i] = Math.min(dp[i], dp[i - value] + 1);
            }
        }

        if (dp[K] == 10001) {
            System.out.println(-1);
        } else {
            System.out.println(dp[K]);
        }
    }
}
