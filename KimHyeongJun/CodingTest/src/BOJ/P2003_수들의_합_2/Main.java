package BOJ.P2003_수들의_합_2;

import java.util.*;
import java.io.*;

public class Main {

    static int N, M;
    static int[] nums;
    static int answer;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));


        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        nums = new int[N];
        st = new StringTokenizer(br.readLine());

        for(int n = 0; n < N; n++) {
            nums[n] = Integer.parseInt(st.nextToken());
        }

        // nums 배열의 i ~ j 번째의 수를 더헀을 때 M이 되는 경우의 수를 구하라
        answer = 0;

        int i = 0, j = 0, sum = nums[0];

        while(j != N) {
            if(sum == M) {
                answer += 1;
                sum -= nums[i++];
            } else if (sum > M) {
                sum -= nums[i++];
            } else  {
                if(N == ++j) {
                    break;
                }
                sum += nums[j];
            }
        }

        br.close();
        bw.write(String.valueOf(answer));
        bw.flush();
        bw.close();
    }

}
