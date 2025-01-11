package BOJ.P15654_N과M_5;

import java.util.*;
import java.io.*;

public class Main {

    static StringBuilder sb = new StringBuilder();
    static int N, M;
    static int[] nums;

    public static void main(String[] args ) throws Exception {
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

        List<Integer> result = new ArrayList<>();
        boolean[] used = new boolean[N];
        Arrays.sort(nums);

        BackTracking(result, used, 0);

        br.close();
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }

    static void BackTracking(List<Integer> result, boolean[] used, int depth) {
        if(depth == M) {
            for(Integer num : result) {
                sb.append(num + " ");
            }
            sb.append("\n");
            return;
        }

        for(int n = 0; n < N; n++){
            if(!used[n]) {
                used[n] = true;
                result.add(nums[n]);
                BackTracking(result, used, depth + 1);
                used[n] = false;
                result.remove(result.size() - 1);
            }
        }
    }
}