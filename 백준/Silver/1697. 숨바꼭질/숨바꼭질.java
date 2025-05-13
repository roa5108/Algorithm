import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;



public class Main {
    static boolean[] visited = new boolean[100001];
    static int N, K;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        System.out.println(bfs(N, K));

    }

    public static int bfs(int loc, int goal) {
        if (loc == goal) return 0;
        Queue<Node> q = new LinkedList<>();
        q.offer(new Node(loc, 0));
        visited[loc] = true;
        while (!q.isEmpty()) {
            Node cur = q.poll();
            int curLoc = cur.vertex;
            int curTime = cur.time;

            int[] nextMoves = {curLoc - 1, curLoc + 1, curLoc * 2};
            for (int nextLoc : nextMoves) {
                if (nextLoc == K) {
                    return curTime + 1;
                } else if (0 <= nextLoc && nextLoc <= 100000 && !visited[nextLoc]) {
                    visited[nextLoc] = true;
                    q.offer(new Node(nextLoc, curTime + 1));
                }
            }
        }
        return -1;
    }

    static class Node {
        int vertex;
        int time;

        Node(int vertex, int time) {
            this.vertex = vertex;
            this.time = time;
        }
    }
}