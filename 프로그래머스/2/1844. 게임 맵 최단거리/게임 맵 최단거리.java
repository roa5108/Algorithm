import java.util.*;

class Solution {
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};
    static int n, m;
    
    public int solution(int[][] maps) {
        n = maps.length;
        m = maps[0].length;
        boolean[][] visited=new boolean[n][m];
        
        bfs(0,0,visited,maps);
        if(maps[n-1][m-1]<=1) return -1;
        return maps[n-1][m-1];
    }
    
    public void bfs(int r, int c, boolean[][] visited, int[][] maps){
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{r,c});
        visited[r][c]=true;
        
        while(!q.isEmpty()){
            int[] cur = q.poll();
            int curR = cur[0];
            int curC = cur[1];
            
            for(int i=0;i<4;i++){
                int nextR = curR + dr[i];
                int nextC = curC + dc[i];
                if(0<=nextR && nextR<n && 0<=nextC && nextC<m && !visited[nextR][nextC] && maps[nextR][nextC]==1){
                    visited[nextR][nextC]=true;
                    maps[nextR][nextC]=maps[curR][curC]+1;
                    q.add(new int[]{nextR,nextC});
                }
            }
        }
    }
}