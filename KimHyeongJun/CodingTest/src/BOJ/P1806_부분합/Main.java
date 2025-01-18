package BOJ.P1806_부분합;

import java.util.*;
import java.io.*;

public class Main {

    static int N, S;
    static int[] nums;
    static int answer;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        S = Integer.parseInt(st.nextToken());

        nums = new int[N];
        st = new StringTokenizer(br.readLine());
        for(int n = 0; n < N; n++) {
            nums[n] = Integer.parseInt(st.nextToken());
        }

        answer = Integer.MAX_VALUE;
        int i = 0, j = 0, sum = nums[0];
        while(true) {
            // sum >= S
            if(sum >= S) {
                answer = Math.min(j - i + 1, answer);
                sum -= nums[i++];
            }
            // sum < S
            else {
                if(N == ++j){
                    break;
                }
                sum += nums[j];
            }
        }

        if(answer == Integer.MAX_VALUE) {
            answer = 0;
        }

        br.close();
        bw.write(String.valueOf(answer));
        bw.flush();
        bw.close();
    }
}
