package BOJ.P1182_부분수열의_합;
import java.util.*;
import java.io.*;

public class Main {

    static int N, S, answer, subCount;
    static int[] nums;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        S = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        nums = new int[N];
        for(int n = 0 ; n < N; n++) {
            nums[n] = Integer.parseInt(st.nextToken());
        }

        answer = 0;

        for(int n = 1; n <= N; n++) {
            subCount = n;
            DFS(0, 0, 0);
        }

        br.close();
        bw.write(String.valueOf(answer));
        bw.flush();
        bw.close();
    }

    static void DFS(int result, int start, int depth) {
        if(depth == subCount) {
            if(result == S) {
                answer += 1;
            }
            return;
        }
        for(int n = start; n < N; n++) {
            DFS(result + nums[n], n + 1, depth + 1);
        }
    }
}