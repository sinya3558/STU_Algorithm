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

        // nums 배열의 i ~ j 번째의 수를 더헀을 떄 M이 되는 경우의 수를 구하라
        // dp를 사용하자
        answer = 0;

        int i = 0, j = 0;
        while(true) {
            if(i == j && nums[i] == M) {
                answer += 1;
                j++;
                if(j == N) {
                    break;
                }
                continue;
            }

            if(getSum(i, j) == M){
                answer += 1;
                j++;
                if(j == N) {
                    break;
                }

            } else if (getSum(i, j) > M) {
                i++;
            } else if(getSum(i, j) < M) {
                j++;
                if(j == N) {
                    break;
                }
            }
        }

        br.close();
        bw.write(String.valueOf(answer));
        bw.flush();
        bw.close();
    }

    static int getSum(int start, int end) {
        int sum = 0;
        for(int k = start; k <= end; k++) {
            sum += nums[k];
        }
        return sum;
    }
}
