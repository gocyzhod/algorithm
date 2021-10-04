import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;
import java.util.* ;

// 15시 15분 시작

public class BOJ_2285 {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st ; //= new StringTokenizer(br.readLine());

        ArrayList<Integer> answer = new ArrayList<Integer>();

        ArrayList<Integer> vil = new ArrayList<Integer>();
        ArrayList<Integer> people = new ArrayList<Integer>();


        int n = Integer.parseInt(br.readLine());

        for (int i =0 ; i < n ; i++){
            st = new StringTokenizer(br.readLine());
            int x,y;
            x = Integer.parseInt(st.nextToken());
            y = Integer.parseInt(st.nextToken());
            vil.add(x);
            people.add(y);
        }

        int tmp = 100000 ;
        int post = 0 ;
        for (int i=0 ; i< n ; i++){
            int place = vil.get(i);
            int think = 0 ;
            if ( n % 2 != 0 ){
                think += Math.abs(place - vil.get(n/2)) * people.get(n/2);
            }
            for (int j = 0 ; j  < n/2 ; j++){
                think += Math.abs(place - vil.get(j)) * people.get(j) ;
                think += Math.abs(place - vil.get(n-j-1))* people.get(j) ;
            }
            if ( think < tmp ) {
                tmp = think ;
                post = i ;
            }
        }

    System.out.println(post+1);

    }

}


// 이분탐색, 삼분탐색 등으로 시간초과를 줄이는게 목표.
