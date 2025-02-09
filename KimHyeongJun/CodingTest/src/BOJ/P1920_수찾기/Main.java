package BOJ.P1920_수찾기;


import java.util.*;
import java.io.*;


// BinarySerach
// 자연수 N, M
// N개의 자연수 , M개의 자연수
// M개의 자연수들이 N개의 자연수 안에 존재하는지 출력

public class Main {

    static int N, M;
    static int[] A, B;
    static StringBuilder sb = new StringBuilder();


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));


        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        A = new int[N];
        st = new StringTokenizer(br.readLine());
        for(int n = 0; n < N; n++) {
            A[n] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        B = new int[M];
        st = new StringTokenizer(br.readLine());
        for(int m = 0; m < M; m++) {
            B[m] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(A);

        for(int m = 0; m < M; m++) {
            Arrays.binarySearch(A, B[m]);
//            sb.append(String.valueOf(BinarySearch(B[m]) + "\n"));
            sb.append(String.valueOf(Arrays.binarySearch(A, B[m]) + "\n"));
        }

        br.close();
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }

    static int BinarySearch(int target) {
        int start = 0, end = N-1;

        while(start <= end) {
            int mid = (start + end) / 2;
            if(A[mid] == target) {
                return 1;
            }
            if (A[mid] > target) {
                end = mid - 1;
            } else {
                start = mid + 1;
            }

        }
        return 0;
    }
}
