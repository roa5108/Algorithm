import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            String line = br.readLine();
            int score = 0;
            int combo = 0;

            for (int j = 0; j < line.length(); j++) {
                if (line.charAt(j) == 'O') {
                    combo++;
                    score += combo;
                } else {
                    combo = 0;
                }
            }
            System.out.println(score);
        }
    }
}
