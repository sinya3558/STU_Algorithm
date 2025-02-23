package BOJ.P1927_최소_힙;

import java.util.*;
import java.io.*;

// Heap
// 최소 힙은 가장 작은 노드가 root에 위치한다.
// N: 연산의 수
// N개의 연산 정보
    // x -> 자연수 -> 값 추가
    // x -> 0 -> 가장 작은 값 출력 후 제거
    // 배열이 비어 있는데 0이 입력으로 들어온 경우 -> 0을 출력
public class Main {

    static int N;

    static int[] heap;
    static StringBuilder sb = new StringBuilder();
    static int heapEndIndex;

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());

        int x;

        // 1 <= N <= 10000이므로 heap의 최대 크기를 100000+1로 지정
            // 인덱스를 1부터 사용하기 위함
        heap = new int[100000+1];
        heapEndIndex = 0;

        for(int n = 0; n < N; n++) {
            st = new StringTokenizer(br.readLine());
            x = Integer.parseInt(st.nextToken());

            // 값 추가
            if(x != 0) {
                add(x);
            }

            // 최소값 출력 후 제거
            else {
                // 배열이 비어 있는데 0이 입력으로 들어온 경우 -> 0을 출력
                if(heapEndIndex == 0) {
                    sb.append(0 + "\n");
                    continue;
                }
                printAndDelete();
            }
        }

        br.close();
        bw.write(sb.toString());
        bw.flush();
        bw.close();

    }

    static void add(int x){
        // heap의 맨 끝에 추가하기
        heapEndIndex += 1;

        heap[heapEndIndex] = x;
        if(heapEndIndex == 1) {
            return;
        }

        int tmpIndex = heapEndIndex;

        while(true){
            if(heap[tmpIndex/2] > heap[tmpIndex]) {
                switchNode(tmpIndex/2, tmpIndex);
                tmpIndex /= 2;
            } else {
                break;
            }
        }
    }

    static void printAndDelete(){
        sb.append(heap[1] + "\n");

        heap[1] = heap[heapEndIndex];
        heap[heapEndIndex] = 0;

        if(heapEndIndex >= 1) {
            heapEndIndex -= 1;
        }

        int tmpIndex = 1;
        int targetIndex;
        while (true) {
            if(heapEndIndex == 1){
                break;
            }

            if(tmpIndex * 2 > heapEndIndex){
                break;
            }

            if(heap[tmpIndex * 2] == 0 && heap[tmpIndex * 2 + 1] == 0) {
                break;
            }

            // 왼쪽 노드 검사
            if(heap[tmpIndex * 2] < heap[tmpIndex * 2 + 1]){
                if(heap[tmpIndex * 2] == 0) {
                    targetIndex =  tmpIndex * 2 + 1;
                } else {
                    targetIndex = tmpIndex * 2;
                }
            }

            // 오른쪽 노드 검사
            else {
                if(heap[tmpIndex * 2 + 1] == 0) {
                    targetIndex = tmpIndex * 2;
                } else {
                    targetIndex =  tmpIndex * 2 + 1;
                }
            }

            if(heap[targetIndex] <= heap[tmpIndex]) {
                switchNode(targetIndex, tmpIndex);
            }

            tmpIndex = targetIndex;

        }
    }

    static void switchNode(int a, int b){
        int tmp = heap[a];
        heap[a] = heap[b];
        heap[b] = tmp;
    }
}
