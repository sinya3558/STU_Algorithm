package BOJ.P9184_신나는_함수_여행;


import java.util.*;
import java.io.*;

public class Main {

    static int[][][] dp;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st;

        dp = new int[21][21][21];
        while(true) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            if(a == -1 && b == -1 && c == -1) {
                break;
            }

            sb.append("w(" + a + ", " + b + ", " + c + ") = " + w(a, b, c)+"\n");
        }

        br.close();
        bw.write(sb.toString());
        bw.flush();
        bw.close();

    }

    static int w(int a, int b, int c) {

        if(check(a, b, c) && dp[a][b][c] != 0) {
            return dp[a][b][c];
        }

        // 3중 하나라도 0보다 작거나 같을 때
        if(a <= 0 || b <= 0 || c <= 0){
            return 1;
        }

        // 3중 하나라도 20보다 클 때
        if(a > 20 || b > 20 || c > 20) {
            return dp[20][20][20] = w(20, 20, 20);
        }

        // a가 b보다 작고, b가 c보다 작을 때
        if(a < b && b < c){
            return dp[a][b][c] = w(a, b,c-1) + w(a,b-1, c-1) - w(a, b-1, c);
        }

        // 3개 다 0보다 크고, 20보다 작거나 같고, (a가 b보다 크거나 같고 || b가 c보다 크거나 같을 때)
        return dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1) ;
    }

    static boolean check(int a, int b, int c) {
        return 0 < a && a <= 20 && 0 < b && b <= 20 && 0 < c && c <= 20;
    }
}
