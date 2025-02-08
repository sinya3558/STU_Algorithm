package BOJ.P1253_좋다;

import java.util.*;
import java.io.*;

// N개의 수
// 어떤 수가 다른 두 수의 합으로 나타낼 수 있으면 GOOD이다.
// N개의 수가 주어지면 그 중에서 좋은 수의 개수는 몇개인지 출력하라.
// 수의 위치가 다르면 값이 같아도 다른 수이다.
// 중복되는 값이 있을 수 있다는 의미
// 특정 값이 두 수의 합이다? -> 특정 값보다 작은 값으로 이루어져 있다.


public class Main {

    static int N;
    static int[] nums;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        if(N < 3) {
            System.out.println(0);
            return;
        }

        nums = new int[N];
        st = new StringTokenizer(br.readLine());
        for(int n = 0; n < N; n++) {
            nums[n] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(nums);

        int answer = 0;

        for (int i = 0; i < N; i++) {
            int target = nums[i];
            int low = 0;
            int high = N - 1;

            while (true) {
                // target을 제외한 다른 두 수이므로 target index가 low 또는 high가 같은 조건 추가
                if(low == i) {
                    low++;
                } else if(high == i) {
                    high--;
                } else {
                    int tmp = nums[low] + nums[high];

                    // 1. target 보다 클 경우 high를 낮춰야 함
                    if(tmp > target) {
                        high--;
                    }
                    // 2. target보다 작을 경우 low를 높여야 함
                    else if (tmp < target) {
                        low++;
                    }
                    else {
                        answer += 1;
                        break;
                    }

                }

                if(low > high || low == high) {
                    break;
                }
            }
        }

        System.out.println(answer);
    }
}
