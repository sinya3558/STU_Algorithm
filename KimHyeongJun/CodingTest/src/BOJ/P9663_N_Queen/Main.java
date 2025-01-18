package BOJ.P9663_N_Queen;

import java.io.*;
import java.util.*;

public class Main {

    static int N;
    static int[] board;
    static int answer;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());

        board = new int[N + 1];

        boolean[] used = new boolean[N + 1];
        answer = 0;
        BackTracking(used, 1);

        br.close();
        bw.write(String.valueOf(answer));
        bw.flush();
        bw.close();
    }

    // 같은 행 X, 같은 열 X, 대각선 X
    static void BackTracking(boolean[] used, int col) {
        if(col == N + 1){
            answer += 1;
            return ;
        }
        for(int row = 1; row <= N; row++){
            if(!used[row]) {
                // board의 col열, row행에 퀸을 놓을 수 있는가?
                if(canPut(col, row)){
                    board[col] = row;
                    used[row] = true;
                    BackTracking(used, col + 1);
                    used[row] = false;
                }
            }
        }
    }

    static boolean canPut(int col, int row) {
        if(col == 1) {
            return true;
        } else {
            for(int c = 1; c < col; c++) {
                // 열이 같을 수 없기에 검사하지 않음 -> 열을 순회 하기 때문
                // 1. 행이 같은지 검사
                // 2. 대각선 검사
                if(board[c] == row || Math.abs(c-col) == Math.abs(board[c] - row)) {
                    return false;
                }
            }
        }
        return true;
    }
}