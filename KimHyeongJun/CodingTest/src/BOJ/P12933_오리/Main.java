package BOJ.P12933_오리;

import java.util.*;
import java.io.*;

// 오리 울음소리는 "quack"
// 올바른 오리 울음 소리는 한번 또는 그 이상 연속해서 내는 것.
// quqacukqauackck 은 오리 2마리가 동시에 운 것.
// 방에 있을 수 있는 최소 오리의 수를 구하시오

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String tmp = br.readLine();

        if(tmp.length() % 5 != 0) {
            System.out.println(-1);
            return ;
        }

        List<String> record = new ArrayList<>();
        for(int i = 0; i < tmp.length(); i++){
            record.add(String.valueOf(tmp.charAt(i)));
        }

        String[] quack = {"q", "u", "a", "c", "k"};
        int quack_index = 0;

        int answer = 0;
        // 오리의 수를 셀 수 있는 경우
        boolean countFlag = false;
        while(true) {
            List<String> tmpRecord = new ArrayList<>();
            // q, u, a, c, k를 순차대로 돌며 탐색
            for(int i = 0; i < record.size(); i++) {
                if(record.get(i).equals(quack[quack_index])) {
                    quack_index += 1;
                    quack_index %= 5;
                    // quack_index가 다시 0이 되었다는 것은 quack 한 단어가 있다는 것
                    // -> 오리가 최소 1마리는 있다는 것
                    if(quack_index == 0) {
                        if(!countFlag) {
                            answer += 1;
                            countFlag = true;
                        }
                    }
                } else {
                    tmpRecord.add(record.get(i));
                }
            }

            // 오리가 탐색 되었을 때
            if(countFlag){
                countFlag = false;
                record = tmpRecord;
                quack_index = 0;
            }

            // 더 이상 탐색된 오리가 없는 경우
            else {
                // 정답이 0이거나, 남은 문자열의 수가 0이 아닐 때
                if(answer == 0 || tmpRecord.size()!=0){
                    answer = -1;
                }
                break;
            }
        }

        System.out.println(answer);

    }

}
