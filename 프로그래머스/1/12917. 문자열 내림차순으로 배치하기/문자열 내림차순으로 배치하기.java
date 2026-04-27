import java.util.*;

class Solution {
    public String solution(String s) {
        char[] charArray = s.toCharArray();
        Arrays.sort(charArray);
        String rev = new StringBuilder(new String(charArray)).reverse().toString();
        return rev;
    }
}