import java.util.*;

class Solution {
    public int solution(String begin, String target, String[] words) {
        Queue<String> q = new ArrayDeque<>();
        Map<String, Boolean> visited = new HashMap<>();
        q.add(begin);
        visited.put(begin,true);
        int depth=0;
        
        while(!q.isEmpty()){
            for(int i=0; i<q.size(); i++){
                String cur=q.remove();
                if(cur.equals(target)) return depth;
                for(String word:words){
                    if(canConvert(cur,word) && !visited.containsKey(word)){
                        q.add(word);
                        visited.put(word,true);
                    }
                }
            }
            depth++;
        }
        return 0;
    }
    
    public boolean canConvert(String now, String next){
        int diff=0;
        for(int i=0; i<now.length(); i++){
            if(now.charAt(i)!=next.charAt(i)) diff++;
        }
        if(diff==1) return true;
        else return false;
    }
}