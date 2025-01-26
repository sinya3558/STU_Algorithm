package BOJ.P15655_N과M_6;

import java.util.*;
import java.io.*;

public class Main {

    static int N, M;
    static int[] nums;
    static StringBuilder sb = new StringBuilder();


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

        Arrays.sort(nums);
        List<Integer> result = new ArrayList<>();
        BackTracking(result, 0, 0);

        br.close();
        bw.write(sb.toString());
        bw.flush();
        bw.close();

    }

    static void BackTracking(List<Integer> result, int start, int depth) {
        if(depth == M) {
            for(Integer num : result) {
                sb.append(num + " ");
            }
            sb.append("\n");
            return ;
        }

        for(int n = start; n < N; n++) {
            result.add(nums[n]);
            BackTracking(result, n + 1, depth + 1);
            result.remove(result.size() - 1);
        }
    }
}
