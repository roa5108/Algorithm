import java.util.*;

class Solution {
    boolean solution(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        for(char ch:s.toCharArray()){
            if(ch=='('){
                stack.add(ch);
            }
            else if(!stack.isEmpty()){
                stack.remove();
            }
            else{
                return false;
            }
        }
        return stack.isEmpty();
    }
}