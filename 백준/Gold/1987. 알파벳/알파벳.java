import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static char[][] map;
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};
    static int R, C;
    static boolean[] alphaVisited;
    static int max = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        map = new char[R][C];
        alphaVisited = new boolean[26];

        for (int i = 0; i < R; i++) {
            String line = br.readLine();
            map[i] = line.toCharArray();
        }

        alphaVisited[map[0][0] - 'A'] = true;
        dfs(0, 0, 1);
        System.out.println(max);

    }

    public static boolean isValid(int row, int col) {
        return 0 <= row && row < R && 0 <= col && col < C;
    }

    public static void dfs(int r, int c, int depth) {
        max = Math.max(max, depth);

        for (int i = 0; i < 4; i++) {
            int curR = r + dr[i];
            int curC = c + dc[i];

            if (isValid(curR, curC)) {
                int index = map[curR][curC] - 'A';
                if (!alphaVisited[index]) {
                    alphaVisited[index] = true; //이 알파벳은 지금 경로에서 씀
                    dfs(curR, curC, depth + 1);
                    alphaVisited[index] = false; //이 경로는 다 끝났으니, 이 알파벳을 다시 써도 됨(백트래킹)
                }
            }
        }
    }
}
