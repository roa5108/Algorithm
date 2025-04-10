import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] arr = new String[5];
        for (int i = 0; i < 5; i++) {
            arr[i] = br.readLine();
        }

        int maxLen = 0;
        for (int i = 0; i < 5; i++) {
            maxLen = Math.max(maxLen, arr[i].length());
        }
        for (int j = 0; j < maxLen; j++) {
            for (int k = 0; k < 5; k++) {
                if (j < arr[k].length()) {
                    System.out.print(arr[k].charAt(j));
                }
            }
        }


    }
}
