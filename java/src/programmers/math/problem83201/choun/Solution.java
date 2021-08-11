package programmers.math.problem83201.choun;

public class Solution {
    public String solution(int[][] scores) {
        StringBuilder answer = new StringBuilder();
        //각 행을 검사하고 결과를 answer에 넣는다.
        int cnt=scores.length;

        for(int i=0;i<cnt;i++){
            int score=scores[i][i];
            int[] max_score=new int[]{0,0};
            int[] min_score=new int[]{100,0};
            float avg=0;
            for(int j=0;j<cnt;j++){
                avg+=scores[j][i];
                if( max_score[0]<scores[j][i]){
                    max_score[0]=scores[j][i];
                    max_score[1]=1;
                }
                else if(max_score[0]==scores[j][i]){
                    max_score[1]++;
                }

                if(min_score[0]>scores[j][i]){
                    min_score[0]=scores[j][i];
                    min_score[1]=1;
                }
                else if(min_score[0]==scores[j][i]){
                    min_score[1]++;
                }
            }

            if((score==max_score[0] && max_score[1]==1) || (score==min_score[0] && min_score[1]==1)){
                avg-=score;
                avg/=(cnt-1);
            }
            else
                avg/=cnt;

            System.out.println(avg);
            if(avg>=90)
                answer.append('A');
            else if(avg>=80 && avg<90)
                answer.append('B');
            else if(avg>=70 && avg<80)
                answer.append('C');
            else if(avg>=50 && avg<70)
                answer.append('D');
            else
                answer.append('F');

        }

        return answer.toString();
    }

    public static void main(String[] args) {
        System.out.println(new Solution().solution(new int[][]{{100,90,98,88,65},{50,45,99,85,77},{47,88,95,80,67},{61,57,100,80,65},{24,90,94,75,65}}));
    }
}
