package baekjoon.search.problem2178.choun;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Main {


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");


        int row= Integer.parseInt(input[0]);
        int col= Integer.parseInt(input[1]);

        int[][] graph=new int[row][col];

        for (int i=0; i<row; i++){
            String s=br.readLine();

            for( int j=0; j<col; j++){
                graph[i][j]=s.charAt(j)-'0';

            }
        }

        System.out.println(bfs(row,col,graph));
    }


    static int bfs(int row, int col, int [][]visited){
        int[] drow={-1,1,0,0};
        int[] dcol={0,0,-1,1};

        Queue<Node> queue=new LinkedList<>();

        visited[0][0]=0;
        queue.add(new Node(0,0,1));


        while (!queue.isEmpty()){
            Node cur=queue.poll();
            if(cur.row==row-1 && cur.col==col-1){
                return cur.cnt;
            }
            for (int i=0; i<4;i++){

                int nr=cur.row+drow[i];
                int nc=cur.col+dcol[i];
                int cnt=cur.cnt;
                if(nr>=0 && nr<row && nc>=0 && nc<col && visited[nr][nc]==1){
                    visited[nr][nc]=0;
                    queue.add(new Node(nr,nc,cnt+1));
                }
            }
        }

        return 0;
    }

    class Node{
        int row, col, cnt;
        Node(int row, int col ,int cnt){
            this.row=row;
            this.col=col;
            this.cnt=cnt;
        }
    }
}

