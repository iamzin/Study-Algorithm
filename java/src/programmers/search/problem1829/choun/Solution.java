

import java.util.*;
public class Solution {
    static int[] dr;
    static int[] dc;

    static class Node{
        int row;
        int col;
        Node(int row, int col){
            this.row=row;
            this.col=col;
        }
    }

    //
    static int bfs(int r, int c, int m, int n, int[][] picture){
        Queue<Node> q=new LinkedList<>();
        int cnt=0;
        int color=picture[r][c];
        q.add(new Node(r,c));
        picture[r][c]=0;
        while(!q.isEmpty()){
            Node cur=q.poll();
            cnt+=1;
            for(int i=0;i<4;i++){
                int nr=cur.row+dr[i];
                int nc=cur.col+dc[i];

                if(nr>=0 && nr<m && nc>=0 && nc<n && picture[nr][nc]==color){
                    q.add(new Node(nr,nc));
                    picture[nr][nc]=0;
                }
            }
        }
        return cnt;
    }

    public int[] solution(int m, int n, int[][] picture) {
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;
        int[] answer = new int[2];
        //좌표에서의 상,하,좌,우 탐색을 위한 배열
        dr=new int[]{-1,1,0,0};
        dc=new int[]{0,0,-1,1};
        //picture 복사
        int[][] p = new int[m][n];
        for(int i=0; i<m; i++) {
            for(int j=0; j<n; j++) {
                p[i][j]=(int)picture[i][j];
            }
        }

        for(int i=0;i<m;i++)
            for(int j=0;j<n;j++){
                //0이 아니면 bfs 탐색 수행
                if (p[i][j]!=0){
                    //영역 수 증가
                    numberOfArea+=1;
                    //영역의 넓이 비교
                    maxSizeOfOneArea= Math.max(maxSizeOfOneArea,bfs(i,j,m,n,p));
                }
            }

        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        System.out.println(Arrays.toString(answer));
        return answer;
    }


    public static void main(String[] args) {
        new Solution().solution(6,4,new int[][]{{1, 1, 1, 0}, {1, 2, 2, 0}, {1, 0, 0, 1}, {0, 0, 0, 1}, {0, 0, 0, 3}, {0, 0, 0, 3}});

    }

}