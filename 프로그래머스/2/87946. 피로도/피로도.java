import java.util.*;

class Solution {
    public int solution(int k, int[][] dungeons) {
        List<List<Integer>> ans = new ArrayList<>();
        boolean[] visited = new boolean[dungeons.length];
        recur(k, dungeons, new ArrayList<>(), ans, visited);
        int maxCnt = 0;
        for (List<Integer> sub : ans) {
            maxCnt = Math.max(maxCnt, sub.size());
        }
        return maxCnt;
    }

    public void recur(int k, int[][] dungeons, List<Integer> curr, List<List<Integer>> ans, boolean[] visited) {
        ans.add(new ArrayList<>(curr));
        for (int i = 0; i < dungeons.length; i++) {
            if (k >= dungeons[i][0]) {
                if (!visited[i]) {
                    curr.add(i);
                    visited[i] = true;
                    recur(k - dungeons[i][1], dungeons, curr, ans, visited);
                    curr.remove(curr.size() - 1);
                    visited[i] = false;
                }
            }
        }
    }
}