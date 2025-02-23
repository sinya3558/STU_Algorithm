package BOJ.P2343_기타_레슨;

import java.util.*;
import java.io.*;

// N개의 강의
// i번 강의와 j번 강의를 같은 블루레이에 녹화하려면 i~j 사이 모든 강의도 같은 블루레이에 있어야 함
// 블루레이의 개수는 최소가 되어야 한다.
// M개의 블루레이에 강의를 잘라서 저장한다
// M개의 블루레이 크기는 모두 같고, 최소이다
// 가능한 블루레이의 최소 크기를 구하여라
public class Main {

    static int N, M;
    static int[] record;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        record = new int[N];
        st = new StringTokenizer(br.readLine());
        int start = Integer.MIN_VALUE;
        int end = 0;
        for(int n = 0; n < N; n++) {
            record[n] = Integer.parseInt(st.nextToken());
            start = Math.max(start, record[n]);
            end += record[n];
        }

        // 1 <= M <= N
        // M이 1인 경우 모든 강의 시간의 합이 되어야 함
        // M이 N인 경우 강의 시간 중 가장 큰 값이 되어야 함
        // 즉, 강의 시간 중 가장 큰 값 <= 블루레이의 최소 크기 <= 최대값은 모든 강의 시간의 합
        // 1개의 블루레이의 최소 크기는 위 범위에 있다
        // 이를 어떻게 찾을 것인가?
        // 이분 탐색으로 찾을 수 있다
        // BinarySearch는 정렬이 되어 있어야 힘
            // Parametric는 정렬과 상관 없이 조건을 만족하는 최소/최대값을 찾는 것

        // start는 최소값이 될 수 있는 후보
        // end는 최대값이 될 수 있는 후보
        // Binary, Parametric Search는 start가 end보다 커지면 종료한다
        // 강의 시간 중 가장 큰 값 <= 블루레이의 최소 크기 <= 최대값
        // 위의 범위에서 블루레이의 최소 크기를 찾고 싶다

        int mid = (start + end) / 2;

        // start가 end보다 클 경우 종료
        while(start <= end) {
            mid = (start + end) / 2;

            int m = getBlurayCount(mid);

            // 블루레이 개수를 늘려야 할 경우
            // 블루레이 개수가 딱 맞을 때 정답인지 아닌지 모른다
                // 해당 값이 최소 크기인지 알 수 없다
                // 시간을 더 줄일 수 있는지 찾아야 한다.
                // 이때 answer=mid일 것이고, 더 줄일 수 있는지 찾기 위해 end를 answer-1으로 설정한다
                // 정답을 찾은 이후로 end는 더이상 줄어들지 않을 것이다
                // 그리고 탐색 종료 시점은 start > end이다.
                // 이때 start = end + 1 = answer이다.
                // 그러므로 탐색이 종료되는 시점의 start가 정답이 된다.
            if(m <= M) {
                end = mid - 1;
            }

            // 블루레이 개수를 줄여야할 경우
            else {
                start = mid + 1;
            }
        }

        System.out.println(start);
    }

    static int getBlurayCount(int m) {
        int tmpSum = 0, blurayCount = 1;
        for(int n = 0; n < N; n++) {
            if(tmpSum + record[n] > m) {
                blurayCount += 1;
                tmpSum = record[n];
            } else {
                tmpSum += record[n];
            }

        }

        return blurayCount;
    }
}
