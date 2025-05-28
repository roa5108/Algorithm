import java.util.*;

class Solution {
    public int solution(String begin, String target, String[] words) {
        Queue<String> q = new ArrayDeque<>();
        Set<String> visited = new HashSet<>();
        int depth=0;
        
        q.add(begin);
        visited.add(begin);
        while(!q.isEmpty()){
            int size=q.size();
            for(int i=0;i<size;i++){
                String cur = q.remove();
                if(cur.equals(target)) return depth;
            for(String word:words){
                if(canConvert(cur,word) && !visited.contains(word)){
                    q.add(word);
                    visited.add(word);
                    }
                }
            }depth++;
        }
        return 0;
    }
    
    public boolean canConvert(String cur, String next){
        int diff=0;
        for(int i=0; i<cur.length(); i++){
            if(cur.charAt(i)!=next.charAt(i)){
                diff++;
            }
        }
        return diff==1;
    }
}