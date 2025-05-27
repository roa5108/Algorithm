import java.util.*;

class Solution {
    public int solution(String begin, String target, String[] words) {
        Queue<String> queue = new ArrayDeque<>();
        queue.add(begin);
        Map<String, Boolean> visited = new HashMap<>();
        int depth =0; //몇단계 거쳤는지
        visited.put(begin,true); //begin부터 bfs 시작
        
        while(!queue.isEmpty()){
            int size = queue.size();
            for(int i=0; i<size; i++){
                String cur = queue.remove();
                if(cur.equals(target)){ //target을 찾으면 depth 리턴 후 종료
                    return depth;
                }
                for(String word:words){
                    if (canConvert(cur,word)&&!visited.containsKey(word)){
                        queue.add(word);
                        visited.put(word,true);
                    }
                }
            }
            depth++;
        }
        return 0;
    }
    
    // 현재 단어와 다음 비교 대상 단어의 알파벳 차이가 1 나면 true
    public boolean canConvert(String cur, String next){
        int diff = 0;
        for(int i=0; i<cur.length(); i++){
            if (cur.charAt(i)!=next.charAt(i)){
                diff++;
            }
        }
        if (diff==1){
            return true;
        }
        return false;
    }
}