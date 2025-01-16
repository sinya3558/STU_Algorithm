package SWA.P1206_View;

import java.util.*;
import java.io.*;

public class Solution {

    static int N;
    static int[] buildingInfo;
    static int answer;
    static StringBuilder sb = new StringBuilder();

    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st;

        int T = 10;

        for(int test_case = 1; test_case <= T; test_case++) {
            st = new StringTokenizer(br.readLine());

            N = Integer.parseInt(st.nextToken());
            buildingInfo = new int[N];

            st = new StringTokenizer(br.readLine());
            for(int n = 0; n < N ; n++) {
                buildingInfo[n] = Integer.parseInt(st.nextToken());
            }

            answer = 0;
            for(int n = 2; n < N - 2 ; n++) {
                int[] height = new int[5];
                int targetHeight = buildingInfo[n];

                for (int i = -2; i < 3; i++) {
                    height[i + 2] = targetHeight - buildingInfo[n + i];
                }

                Arrays.sort(height);

                if (height[1] <= 0) {
                    continue;
                }

                answer += height[1];
            }
            sb.append("#" + test_case + " " + answer + "\n");
        }
        br.close();
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}