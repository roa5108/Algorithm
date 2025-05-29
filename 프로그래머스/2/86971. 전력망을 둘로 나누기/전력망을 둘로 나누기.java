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
            int count = dfs(1, visited, tree);
            int diff = Math.abs(n-2*count);
            answer=Math.min(diff, answer);
        }
        return answer;
    }
    
    public int dfs(int node, boolean[] visited, List<List<Integer>> tree){
        visited[node]=true;
        int count=1;
        for(int next : tree.get(node)){
            if(!visited[next]){
                count += dfs(next, visited, tree);
            }
        }
        return count;
    }
}