package BOJ.P16987_계란으로_계란치기;

import java.util.*;
import java.io.*;

// 계란에는 내구도와 무게가 있따
// 각 계란끼리 쳤을 때 각 계란의 내구도는 상대 계란의 무게만큼 깎인데
// 내구도가 0이하가 되면 계란은 깨진다
// 예)
// 계란1 (내구도 7, 무게 5)
// 계란2 (내구도 3, 무게 4)
// 서로 치고난 후
// 계란1 (내구도 3, 무게 5)
// 계란2 (내구도 -2, 무게 4) -> 깨짐

// 일렬로 놓여있는 계란에 대해 왼쪽부터 차례로 들어서 한 번씩만 다른 계란을 쳐 최대한 많은 계란을 깨는 문제

// 1. 가장 왼쪽의 계란을 든다.
// 2. 손에 들고 있는 계란으로 깨지지 않은 다른 계란 중에서 하나를 친다.
// 단, 손에 든 계란이 깨졌거나 깨지지 않은 다른 계란이 없으면 치지 않고 넘어간다.
// 이후 손에 든 계란을 원래 자리에 내려놓고 3번 과정을 진행한다.
// 3. 가장 최근에 든 계란의 한 칸 오른쪽 계란을 손에 들고 2번 과정을 다시 진행한다.
// 단, 가장 최근에 든 계란이 가장 오른쪽에 위치한 계란일 경우 계란을 치는 과정을 종료한다.

// 최대한 많은 계란을 깨는 것이 목표


public class Main {

    static int N, answer;
    static int[] naegudo, weights, tmp;
    static boolean[] visited;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());

        naegudo = new int[N];
        weights = new int[N];
        for(int n = 0 ; n < N; n++) {
            st = new StringTokenizer(br.readLine());
            naegudo[n] = Integer.parseInt(st.nextToken());
            weights[n] = Integer.parseInt(st.nextToken());
        }

        answer = Integer.MIN_VALUE;

        tmp = new int[4];
        visited = new boolean[4];

        // index: 계란의 index
        BackTracking(0);

        System.out.println(answer);

    }

    static void BackTracking(int index) {
        // 마지막 계란까지 모두 사용한 경우
        // 깨진 계란(내구도가 0이하인 계란)의 수를 샌다
        if(index == N) {
            int brokenCount = 0;
            for(int n = 0; n < N; n++){
                if(naegudo[n] <= 0) {
                    brokenCount++;
                }
            }
            answer = Math.max(answer, brokenCount);
            return;
        }

        // 손에 든 계란의 내구도가 0이하일 경우
        // 다음으로 계란(오른쪽에 있는 계란) 선택
        if(naegudo[index] <= 0) {
            BackTracking(index + 1);
            return;

        }

        boolean hit = false;
        for(int i = 0; i < N; i++) {
            if(i == index || naegudo[i] <= 0) {
                continue;
            }

            hit = true;
            naegudo[index] -= weights[i];
            naegudo[i] -= weights[index];

            BackTracking(index + 1);

            naegudo[index] += weights[i];
            naegudo[i] += weights[index];
        }

        if(!hit) {
            BackTracking(index + 1);
        }
    }
}
