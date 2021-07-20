import java.io.*;

public class Main {

    public static void main(String[] args) throws NumberFormatException, IOException{

        BufferedReader input  = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String arr1= input.readLine();
        String arr2 = input.readLine();

        int answer = 0;

        for ( int i = 0 ; i < arr1.length()-arr2.length() + 1 ; i++) {

            String temp = arr1.substring(i, i + arr2.length());
            if (temp.equals(arr2)) {

                answer++;
                i += arr2.length();
                i--;

            }
        }
            bw.write(answer + "\n");

            bw.flush();
            input.close();
            bw.close();

    }
}
