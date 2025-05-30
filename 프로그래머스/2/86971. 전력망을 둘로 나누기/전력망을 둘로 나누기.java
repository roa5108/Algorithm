import java.util.*;

class Solution {
    public int solution(int n, int[][] wires) {
        int answer = Integer.MAX_VALUE;
        
        for(int i=0; i<wires.length; i++){
            List<List<Integer>> tree = new ArrayList<>();
            for(int j=0; j<=n; j++){
                tree.add(new ArrayList<>());
            }
            
            for(int j=0; j<wires.length; j++){
                if(i==j) continue;
                tree.get(wires[j][0]).add(wires[j][1]);
                tree.get(wires[j][1]).add(wires[j][0]);
            }
            boolean[] visited = new boolean[n+1];
            int count = dfs(1,tree,visited);
            int diff=Math.abs(n-2*count);
            answer=Math.min(answer,diff);
        }
        return answer;
    
    }
    
    public int dfs(int node, List<List<Integer>> tree, boolean[] visited){
        int count=1;
        visited[node]=true;
        for(int next:tree.get(node)){
            if(!visited[next]){
                count+=dfs(next, tree, visited);
            }
        }
        return count;
    }
}