import java.util.*;

class Solution {
     public int solution(int n, int[][] wires) {
        int answer = Integer.MAX_VALUE;

        // 간선 하나씩 제거해보는 반복문
        for (int i = 0; i < wires.length; i++) {
            List<List<Integer>> tree = new ArrayList<>();
            for (int j = 0; j <= n; j++) {
                tree.add(new ArrayList<>());
            }

            for (int j = 0; j < wires.length; j++) {
                if (i == j) continue; // i번째 간선은 제외하고 그래프를 구성
                int a = wires[j][0];
                int b = wires[j][1];
                tree.get(a).add(b);
                tree.get(b).add(a);
            }
            boolean[] visited = new boolean[n + 1]; // 방문 배열
            int count = dfs(1, tree, visited); // 하나의 연결된 송전탑 개수

            int diff = Math.abs(n - 2 * count); //Math.abs((n - count) - count)와 같음;

            answer = Math.min(answer, diff); // 최소 차이 갱신
        }
        return answer;
    }

    public int dfs(int node, List<List<Integer>> tree, boolean[] visited) {
        visited[node] = true;
        int count = 1;
        for (int next : tree.get(node)) {
            if (!visited[next]) {
                count += dfs(next, tree, visited);
            }
        }
        return count;
    }
}