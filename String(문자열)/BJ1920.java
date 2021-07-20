import java.awt.print.Pageable;
import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BJ1920 {


    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));


        int n = Integer.parseInt(br.readLine());
        int[] arr1 = new int[n];
        StringTokenizer stringTokenizer = new StringTokenizer(br.readLine());
        for( int i = 0 ; i < n ; i++){
            arr1[i] = Integer.parseInt(stringTokenizer.nextToken());
        }


        int m = Integer.parseInt(br.readLine());
        int[] arr2 = new int[m];
        StringTokenizer stringTokenizer1 = new StringTokenizer(br.readLine());
        for ( int i = 0 ; i < m ; i ++ ){
            arr2[i] = Integer.parseInt(stringTokenizer1.nextToken());
        }

        String answer = "";


        Arrays.sort(arr1); // 오름차순 정렬
        Arrays.sort(arr2);

        int start = 0;
        int end = arr2.length - 1 ;
        int position1 = 0 ;
        int position2 = arr1.length - 1 ;

        if ( n > 1 && m > 1 ) {

            while (true) {

                if (arr1[position1] > arr2[start]) {
                    answer = '0' + answer;
                    start++;
                    
                    bw.append('0');

                } else if (arr1[position1] < arr2[start]) {
                    position1++;
                } else if (arr1[position1] == arr2[start]) {
                    answer = '1' + answer;
                    position1++;
                    start++;
                    bw.append('1');

                }
                if (arr1[position2] > arr2[end]) {
                    position2--;
                } else if (arr1[position2] < arr2[end]) {
                    bw.append('0');
                    answer = answer + '0';
                    end--;
                } else if (arr1[position2] == arr2[end]) {
                    answer = answer + '1';
                    position2--;
                    end--;
                    bw.append('1');

                }
                if (start >= end || position1 >= position2) {
                    break;
                }

            }
        }
        else if ( n == 1 && m > 1 ){
            if (arr1[0] == arr2[start] || arr1[0] == arr2[end]){
                System.out.println("1");
            }
            else {
                System.out.println("0");
            }
        }
        else if ( n != 1 && m == 1){
            if ( arr1[position1] == arr2[0] || arr1[position2]== arr2[0] ){
                System.out.println("1");
            }
            else{
                System.out.println("0");
            }
        }
        //char[] answerarr = new char[answer.length()];
        for ( int i = 0 ; i < m ; i ++){

            //answerarr[i] = answer.charAt(i);
            System.out.println(answer.charAt(i));
        }

        bw.close();
        br.close();

    }
}
