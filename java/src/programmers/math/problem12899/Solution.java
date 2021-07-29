package programmers.math.problem12899;

public class Solution {
    public String solution(int n) {
        String answer = "";
        String[] numbers={"1","2","4"};
        int cnt=1;
        n-=1;
        while (true){
            if(n-(int)Math.pow(3,cnt)>=0){
                n-=(int)Math.pow(3,cnt);
                cnt+=1;
            }
            else
                break;
        }

        while(cnt>0){
            int tmp=(int)Math.pow(3,cnt-1);
            int idx=n/tmp;
            n=n%tmp;
            cnt-=1;
            answer+=numbers[idx];



        }
        System.out.println(answer);
        return answer;
    }

    public static void main(String[] args) {
        new Solution().solution(11);
    }

}