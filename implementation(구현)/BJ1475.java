import java.util.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.LinkedList;

public class BJ1475 {

    static int n ;
    //static int[] card ;
    public static void main(String[] args) throws IOException {


        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        int[] card = {0,0,0,0,0,0,0,0,0,0};
        String temp = Integer.toString(n);
        int[] number = new int[temp.length()];
        for ( int i = 0 ; i < temp.length() ; i ++){

            number[i] = temp.charAt(i) - '0' ;
        }
        int think = 0;
        while(true){

            if( number[think] == 9 ) {
                number[think] = 6 ;
            }

            card[number[think]] += 1;

            think += 1;
            if ( think >= number.length ){
                if ( card[6] % 2 != 0 ){
                    card[6] += 1;
                    card[6] = card[6] / 2 ;
                }
                else if ( card[6] % 2 == 0 ){
                    card[6] /= 2;
                }
                break;
            }
        }


        Arrays.sort(card);

        System.out.println(card[card.length-1]);

    }

}
