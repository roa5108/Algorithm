import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[][] arr = new int[9][9];

        int maxN = -1;
        int idx1 = 0;
        int idx2 = 0;
        for (int i = 0; i < 9; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            for (int j = 0; j < 9; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
                if (maxN < arr[i][j]) {
                    maxN = arr[i][j];
                    idx1 = i + 1;
                    idx2 = j + 1;
                }
            }
        }
        System.out.println(maxN);
        System.out.println(idx1 + " " + idx2);
    }
}