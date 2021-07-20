import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int m , n ;
    static int[][] map ;
    static int[] dx = {1,0,-1,0};
    static int[] dy = {0,1,0,-1};
    static boolean[][] visited ;
    static int answer = 0;

    public static void main(String[] args) throws IOException{



        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());

        map = new int[m][n];
        visited = new boolean[m][n];
        for (int i =0; i<m ; i++){

            String line = br.readLine();

            for (int j = 0 ; j<n ; j ++){
                map[i][j] = line.charAt(j)-'0';
                //visited[i][j] = false;
            }
        }



        for ( int j =0 ; j < n ; j++){

            if ( visited[0][j] == false && map[0][j] == 0 ){

                dfs(0,j);
                visited[0][j] = false;
                if (answer == 1){
                    break;
                }
            }

        }

        if ( answer == 1){
            System.out.println("YES");
        }
        else{
            System.out.println("NO");
        }


        //System.out.println(Arrays.deepToString(map));
        //https://hianna.tistory.com/511
    }

    static void dfs(int x,int y){
/*
        if ( x == m-1 ){
            return ;
        }

 */
        visited[x][y] = true;
        for(int i =0 ; i < 4; i ++ ){
            int nx = dx[i] + x;
            int ny = dy[i] + y;
            if ( 0<= nx && nx < m && 0<= ny && ny < n ){

                if ( visited[nx][ny] == false && map[nx][ny] == 0 ){
                    if ( nx == m- 1 ){
                        answer = 1;
                        return ;
                    }
                    else {
                        dfs(nx, ny);
                        //visited[nx][ny] = false;
                    }
                }

            }

        }



    }

}
