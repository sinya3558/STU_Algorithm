package BOJ.P15663_N과M_9;

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
        boolean[] visited = new boolean[N];
        BackTracking(result, visited);

        br.close();
        bw.write(sb.toString());
        bw.flush();
        bw.close();


    }

    static void BackTracking (List<Integer> result, boolean[] visited) {
        int before = 0;
        if(result.size() == M) {
            for(Integer num : result) {
                sb.append(num + " ");
            }

            sb.append("\n");
            return ;
        }

        for(int n = 0; n < N; n++){
            if(!visited[n]) {
                if(before == nums[n]){
                    continue;
                }

                visited[n] = true;
                result.add(nums[n]);

                BackTracking(result, visited);

                visited[n] = false;
                result.remove(result.size() - 1);
                before = nums[n];
            }
        }
    }
}
