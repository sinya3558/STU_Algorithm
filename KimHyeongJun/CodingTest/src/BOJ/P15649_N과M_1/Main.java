package BOJ.P15649_N과M_1;

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

        nums = new int[N+1];
        for(int n = 1; n <= N; n++) {
            nums[n] = n;
        }

        boolean[] used = new boolean[N+1];
        List<Integer> result = new ArrayList<>();
        BackTracking(used, result);

        br.close();
        bw.write(sb.toString());
        bw.flush();
        bw.close();

    }


    static void BackTracking(boolean[] used, List<Integer> result) {
        if(result.size() == M) {
            for(Integer num: result){
                sb.append(num+" ");

            }
            sb.append("\n");

            return ;
        }


        for(int n = 1; n <= N; n++) {
            if(!used[n]) {
                used[n] = true;
                result.add(n);
                BackTracking(used, result);
                used[n] = false;
                result.remove(result.size() - 1);
            }
        }
    }
}
