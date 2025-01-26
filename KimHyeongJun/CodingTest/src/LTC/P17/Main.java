package LTC.P17;

import java.util.*;
import java.io.*;

class Solution {
    String[] keypad = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};

    Solution(){}

    public List<String> letterCombinations(String digits) {
        List<String> result = new ArrayList<>();


        StringBuilder tmp = new StringBuilder();
        char[] digitsArray = digits.toCharArray();
        if(digits.length() != 0){
            BackTracking(result, tmp, digitsArray, 0);
        }

        return result;
    }

    public void BackTracking(List<String> result, StringBuilder tmp, char[] digitsArray, int depth){
        if(depth == digitsArray.length) {
            result.add(tmp.toString());
            return;
        }

        for(char alphabet : keypad[Character.getNumericValue(digitsArray[depth])].toCharArray()) {
            tmp.append(alphabet);
            BackTracking(result, tmp, digitsArray, depth + 1);
            tmp.deleteCharAt(depth);
        }
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));


        Solution solution = new Solution();

        for(int i = 0; i < 3; i++){
            List<String> result = solution.letterCombinations(br.readLine());
            bw.write(result.toString());
            bw.flush();
        }

        br.close();
        bw.close();
    }
}
