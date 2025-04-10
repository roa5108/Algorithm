import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String S = br.readLine();

        int[] alpha = new int[26];
        Arrays.fill(alpha, -1);

        for (int i = 0; i < S.length(); i++) {
            if (alpha[S.charAt(i) - 97] == -1) {
                alpha[S.charAt(i) - 97] = i;
            }
        }
        for (int i = 0; i < 26; i++) {
            System.out.print(alpha[i] + " ");
        }
    }
}
