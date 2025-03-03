package BOJ.P1932_정수_삼각형;

import java.util.*;
import java.io.*;

// DP

// 삼각형의 꼭대기에서 아래에 있는 수 중 하나를 선택
// 맨 아래까지 내려올 때 선택된 수들의 합의 최대는?


public class Main {

    static int N;
    static List<Integer>[] triangle;
    static List<Integer>[] dp;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());

        triangle = new ArrayList[N+1];
        dp = new ArrayList[N+1];
        for(int n = 1; n <= N; n++) {
            triangle[n] = new ArrayList<>();
            dp[n] = new ArrayList<>();
            st = new StringTokenizer(br.readLine());
            for(int i = 0; i < n; i++) {
                triangle[n].add(Integer.parseInt(st.nextToken()));
            }
        }

        dp[1].add(triangle[1].get(0));
        if(N == 1) {
            System.out.println(dp[1].get(0));
            return;
        }

        // 삼각형을 한 층씩 내려가며 부모와 더했을 때 더 큰 값을 dp에 저장
        int answer = 0;
        for(int n = 2; n <= N; n++) {
            for(int i = 0; i < n; i++) {
                int current = triangle[n].get(i);
                // 왼쪽 맨 끝 노드
                if(i == 0) {
                    dp[n].add(current + dp[n-1].get(i));
                }
                // 오른쪽 맨 끝 노드
                else if (i == n-1) {
                    dp[n].add(current + dp[n-1].get(i-1));
                }
                // 중간 노드
                else {
                    dp[n].add(current + Math.max(dp[n-1].get(i-1), dp[n-1].get(i)));
                }
                answer = Math.max(answer, dp[n].get(dp[n].size() - 1));
            }
        }

        System.out.println(answer);
    }
}

