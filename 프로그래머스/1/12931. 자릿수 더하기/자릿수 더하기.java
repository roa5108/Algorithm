import java.util.*;

public class Solution {
    public int solution(int n) {
        String N=String.valueOf(n);
        int answer=0;
        for (int i=0; i<N.length(); i++){
            answer+=N.charAt(i)-'0';
        }
        return answer;
    }
}