package BOJ.P2143_두_배열의_합;

import java.util.*;
import java.io.*;

// TwoPointer
public class Main {

    static int T, N, M;
    static int[] A, B;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        T = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        A = new int[N];
        for(int n = 0; n < N; n++) {
            A[n] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        B = new int[M];
        for(int m = 0; m < M; m++) {
            B[m] = Integer.parseInt(st.nextToken());
        }

        List<Long> subA = new ArrayList<>();
        for(int i = 0; i < N; i++){
            long sum = 0;
            for(int j = i; j < N; j++) {
                sum += A[j];
                subA.add(sum);
            }
        }

        List<Long> subB = new ArrayList<>();
        for(int i = 0; i < M; i++){
            long sum = 0;
            for(int j = i; j < M; j++) {
                sum += B[j];
                subB.add(sum);
            }
        }

        Collections.sort(subA);
        Collections.sort(subB, Collections.reverseOrder());


        long answer = 0;
        int idxA = 0, idxB = 0;

        while(idxA < subA.size() && idxB < subB.size()) {
            long targetA = subA.get(idxA);
            long targetB = T - targetA;

            if (subB.get(idxB) == targetB) {
                long countA = 0;
                long countB = 0;

                while(idxA < subA.size() && subA.get(idxA) == targetA) {
                    countA += 1;
                    idxA++;
                }

                while(idxB < subB.size() && subB.get(idxB) == targetB) {
                    countB += 1;
                    idxB++;
                }
                answer += countA * countB;
            }
            else if (subB.get(idxB) > targetB) {
                idxB += 1;
            }
            else {
                idxA += 1;
            }
        }

        br.close();
        bw.write(String.valueOf(answer));
        bw.flush();
        bw.close();
    }
}

//// Hash
//public class Main {
//
//    static int T, N, M;
//    static int[] A, B;
//
//    public static void main(String[] args) throws Exception {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
//
//        StringTokenizer st = new StringTokenizer(br.readLine());
//        T = Integer.parseInt(st.nextToken());
//
//        st = new StringTokenizer(br.readLine());
//        N = Integer.parseInt(st.nextToken());
//
//        st = new StringTokenizer(br.readLine());
//        A = new int[N];
//        for(int n = 0; n < N; n++) {
//            A[n] = Integer.parseInt(st.nextToken());
//        }
//
//        st = new StringTokenizer(br.readLine());
//        M = Integer.parseInt(st.nextToken());
//
//        st = new StringTokenizer(br.readLine());
//        B = new int[M];
//        for(int m = 0; m < M; m++) {
//            B[m] = Integer.parseInt(st.nextToken());
//        }
//
//        Map<Long, Long> mapA = new HashMap<>();
//        for(int i = 0; i < N; i++){
//            long sum = 0;
//            for(int j = i; j < N; j++) {
//                sum += A[j];
//                Long tmp = mapA.get(sum);
//                if(tmp == null) {
//                    tmp = 0l;
//                }
//                mapA.put(sum, tmp + 1);
//            }
//        }
//
//        Map<Long, Long> mapB = new HashMap<>();
//        for(int i = 0; i < M; i++){
//            long sum = 0;
//            for(int j = i; j < M; j++) {
//                sum += B[j];
//                Long tmp = mapB.get(sum);
//                if(tmp == null) {
//                    tmp = 0l;
//                }
//                mapB.put(sum, tmp + 1);
//            }
//        }
//
//        long answer = 0;
//        for(Long keyA : mapA.keySet()) {
//            Long numB = mapB.get(T - keyA);
//            if(numB == null) {
//                continue;
//            }
//
//            answer += mapA.get(keyA) * numB;
//        }
//
//        br.close();
//        bw.write(String.valueOf(answer));
//        bw.flush();
//        bw.close();
//    }
//}