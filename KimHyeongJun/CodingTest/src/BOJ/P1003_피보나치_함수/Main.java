package BOJ.P1003_피보나치_함수;

import java.util.*;
import java.io.*;

public class Main {

    static StringBuilder sb = new StringBuilder();
    static int N;
    static int[] dpZero, dpOne;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int T = Integer.parseInt(st.nextToken());

        for(int test_case = 0; test_case < T; test_case++) {
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());

            dpZero = new int[N+1];
            dpOne = new int[N+1];

            dpZero[0] = 1;
            dpOne[0] = 0;

            if(N >= 1){
                dpZero[1] = 0;
                dpOne[1] = 1;
            }

            if(N > 1) {
                getZeroOneCount();
            } else {
                sb.append(dpZero[N]+" "+dpOne[N]+"\n");
            }
        }

        br.close();
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }

    static void getZeroOneCount(){
        for(int idx = 2; idx <= N; idx++) {
            dpZero[idx] = dpZero[idx-1] + dpZero[idx-2];
            dpOne[idx] = dpOne[idx-1] + dpOne[idx-2];
        }

        sb.append(dpZero[N]+" "+dpOne[N]+"\n");
    }
}
