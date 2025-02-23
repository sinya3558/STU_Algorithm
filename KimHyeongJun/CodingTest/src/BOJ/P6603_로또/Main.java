package BOJ.P6603_로또;


import java.util.*;
import java.io.*;


// 독일 로또는 1~49 중 6개 숫자를 고른다
// k(k>6)개의 수를 골라 집합 S를 만들고 해당 수로만 번호를 선택
// k=8, S={1,2,3,5,8,13,21,34}인 경우 이 집합 S에서 수를 고를 수 있는 경우의 수는 총 28가지이다.
// ([1,2,3,5,8,13], [1,2,3,5,8,21], [1,2,3,5,8,34], [1,2,3,5,13,21], ..., [3,5,8,13,21,34])

// 집합 S와 k가 주어졌을 때 수를 고르는 모든 방법

public class Main {


    static int K;
    static int[] S, result;
    static StringBuilder sb = new StringBuilder();


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st;
        while(true) {
            st = new StringTokenizer(br.readLine());
            K = Integer.parseInt(st.nextToken());

            if(K == 0) {
                break;
            }

            S = new int[K];
            for(int k = 0; k < K; k++) {
                S[k] = Integer.parseInt(st.nextToken());
            }

            result = new int[6];
            BackTracking(0, 0);
            sb.append("\n");
        }

        br.close();
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }

    // 다음 반복에 현재 값 다음부터 시작해야 하므로 start는 n + 1로 지정해준다
    static void BackTracking(int start, int depth) {
        if(depth == 6) {
            for(int num : result) {
                sb.append(num+" ");
            }
            sb.append("\n");
            return;
        }

        for(int s = start; s < S.length; s++) {
            result[depth] = S[s];
            BackTracking(s + 1, depth + 1);
        }
    }
}
