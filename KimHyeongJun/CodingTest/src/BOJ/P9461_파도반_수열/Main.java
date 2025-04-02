package BOJ.P9461_파도반_수열;


import java.util.*;
import java.io.*;

// DP

public class Main {

    static int N;
    static long[] triangle;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int T = Integer.parseInt(st.nextToken());


        for(int test_case = 0; test_case < T; test_case++) {
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());

            if(N <= 5) {
                if(N <= 3){
                    sb.append(1 + "\n");
                    continue;
                } else {
                    sb.append(2 + "\n");
                    continue;
                }
            }

            triangle = new long[N+1];

            triangle[1] = 1;
            triangle[2] = 1;
            triangle[3] = 1;
            triangle[4] = 2;
            triangle[5] = 2;

            for(int n = 6; n <= N; n++) {
                triangle[n] = triangle[n-1] + triangle[n-5];
            }

            sb.append(triangle[N] + "\n");
        }

        br.close();
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}
