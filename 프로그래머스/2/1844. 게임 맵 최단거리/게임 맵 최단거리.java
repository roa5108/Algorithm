import java.util.*;

class Solution {
    static int[] dr = {-1,1,0,0};
    static int[] dc = {0,0,-1,1};
    static int n, m;
    
    public int solution(int[][] maps) {
        n=maps.length;
        m=maps[0].length;
        boolean[][] visited = new boolean[n+1][m+1];
        
        bfs(0,0,visited,maps);
        if(maps[n-1][m-1]<=1) {
            return -1;
        }
        else{
            return maps[n-1][m-1];
        }
    }
    
    public void bfs(int r, int c, boolean[][] visited, int[][] maps){
        Queue<int[]> q = new ArrayDeque<>();
        q.add(new int[]{r,c});
        visited[r][c]=true;
        
        while(!q.isEmpty()){
            int[] cur=q.remove();
            int cr=cur[0];
            int cc=cur[1];
            
            for(int i=0; i<4; i++){
            int nr=cr+dr[i];
            int nc=cc+dc[i];
            if(0<=nr && nr<n && 0<=nc && nc<m && !visited[nr][nc] && maps[nr][nc]==1){
                q.add(new int[]{nr,nc});
                visited[nr][nc]=true;
                maps[nr][nc]=maps[cr][cc]+1;
            }
        }
        }
        
        
    }
}