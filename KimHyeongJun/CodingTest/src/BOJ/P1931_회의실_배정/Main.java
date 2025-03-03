package BOJ.P1931_회의실_배정;


import java.util.*;
import java.io.*;

// Greedy
// 1개의 회의실, N개 회의에 대한 회의실 사용표 제작
// 회의가 겹치지 않게 회의실을 사용할 수 있는 최대 개수
// 회의가 끝남과 동시에 시작 가능
// 시작 및 끝는 시간이 같을 수 있음(시작하자마자 끝나는 것)

// 0부터 마지막 시간까지 회의를 선택할 때 가장 짧은 순서대로 회의를 선택
// 회의가 끝나는 시간 기준 오름차순 정렬
// 끝나는 시간이 같다면 시작 시간 기준 오름 차순 정렬

// 올바르지 않은 정렬
// 1 3
// 8 8
// 4 8

// 위는 시작 시간을 고려하지 않았을 때 결과이다.
// 시작 시간과 종료 시간이 같은 경우 역시 count 되어야 하므로 시작 시간 역시 오름차순이 되어야 한다.

// 올바른 정렬
// 1 3
// 4 8
// 8 8

class Meeting implements Comparable<Meeting> {
    int start;
    int end;
    Meeting(int start, int end) {
        this.start = start;
        this.end = end;
    }

    @Override
    public int compareTo(Meeting o) {
        if (this.end == o.end) {
            return Integer.compare(this.start, o.start);  // 시작 시간 오름차순 정렬 추가
        }
        return Integer.compare(this.end, o.end);
    }
}

public class Main {

    static int N;
    static List<Meeting> meetingList;
    static int answer;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());

        meetingList = new ArrayList<>();

        for(int n = 0; n < N; n++) {
            st = new StringTokenizer(br.readLine());
            meetingList.add(
                    new Meeting(
                            Integer.parseInt(st.nextToken()),
                            Integer.parseInt(st.nextToken())
                    )
            );
        }

        Collections.sort(meetingList);

        int prevEnd = -1;
        answer = 0;
        for(Meeting meeting: meetingList){
            if(prevEnd > meeting.start) {
                continue;
            }
            answer += 1;
            prevEnd = meeting.end;
        }

        System.out.println(answer);
    }
}


//
//// 시간 초과
//public class Main {
//
//    static int N;
//    static List<Meeting> meetingList;
//    static int answer;
//
//
//    public static void main(String[] args) throws Exception {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
//
//        StringTokenizer st = new StringTokenizer(br.readLine());
//
//        N = Integer.parseInt(st.nextToken());
//
//        meetingList = new ArrayList<>();
//        for(int n = 0; n < N; n++) {
//            st = new StringTokenizer(br.readLine());
//            meetingList.add(
//                    new Meeting(
//                            Integer.parseInt(st.nextToken()),
//                            Integer.parseInt(st.nextToken())
//                    )
//            );
//        }
//        answer = 0;
//
//        Collections.sort(meetingList);
//
//        DFS(0, 0, -1, 0);
//
//        System.out.println(answer);
//    }
//
//    static void DFS(int count, int start, int prevEnd, int depth) {
//        if(depth == N) {
//            answer = Math.max(answer, count);
//            return;
//        }
//
//        for(int n = start; n < N; n++) {
//            // 선택할 수 없을 때
//            if(prevEnd > meetingList.get(n).start) {
//                DFS(count, n + 1, prevEnd, depth + 1);
//                continue;
//            }
//
//            // 선택할 수 있을 때
//            // 1. 선택했을 때
//            DFS(count + 1, n + 1, meetingList.get(n).end, depth + 1);
//
//            // 2. 선택 안했을 때
//            DFS(count, n + 1, prevEnd, depth + 1);
//        }
//    }
//}
