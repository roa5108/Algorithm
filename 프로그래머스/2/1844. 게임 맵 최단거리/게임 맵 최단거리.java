import java.util.*;

class Solution {
    static int[] dr={-1,1,0,0};
    static int[] dc={0,0,-1,1};
    
    public int solution(int[][] maps) {
        int n=maps.length;
        int m=maps[0].length;
        boolean[][] visited = new boolean[n+1][m+1];
        Queue<int[]> q = new ArrayDeque<>();
        q.add(new int[]{0,0});
        while(!q.isEmpty()){
            int[] cur=q.remove();
            int r=cur[0];
            int c=cur[1];
            for(int i=0; i<4; i++){
                int nr=r+dr[i];
                int nc=c+dc[i];
                if(0<=nr && nr<n && 0<=nc && nc<m && !visited[nr][nc] && maps[nr][nc]==1){
                    q.add(new int[]{nr,nc});
                    visited[nr][nc]=true;
                    maps[nr][nc]=maps[r][c]+1;
                }
            }
        }
        
        if(maps[n-1][m-1]<=1) return -1;
        else return maps[n-1][m-1];
        
    }
}