package programmers.weeklychallenge.problem82612.choun;

public class Solution {
    public long solution(int price, int money, int count) {
        long answer = -1;

        long sum=0;
        for (int i=1;i<=count;i++){
            sum+=(long)(i*price);
        }
        if ((long)(money-sum)>0)
            return 0;
        else
            return (long)(sum-money);

    }

    public static void main(String[] args) {
        System.out.println(new Solution().solution(3,20,4));
    }
}