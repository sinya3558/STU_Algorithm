package PGS.주식가격;


// 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때,
// 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

public class Solution {
    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];

        for(int i = 0; i < prices.length; i++) {
            int tmp = prices[i];
            int second = 0;
            for(int j = i+1; j < prices.length; j++) {
                if(tmp <= prices[j]) {
                    second += 1;
                } else {
                    second += 1;
                    break;
                }
            }
            answer[i] = second;

        }

        return answer;
    }

    public static void main(String[] args) {
        int[] test = {1, 2, 3, 2, 3};
        Solution solution = new Solution();
        solution.solution(test);
    }
}
