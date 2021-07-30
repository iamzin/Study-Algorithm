package programmers.math.problem12899.chae;

public class NumberOf124World {
    /*
     * 프로그래머스 - 123 나라의 숫자 PS 1,2,4,11,12,14,21,22,24,41,42,44,111,112,114,... 3 단위로
     * 바뀜 (3 진법 활용 필요) -> 124 나라 : 1,2,4 = 3진법 : 1,2,0 => 3으로 나눠 떨어지면 0 대신 4가 들어가고
     * 몫에서 1을 빼줘야함
     */
    public String solution(int n) {
        StringBuilder answer = new StringBuilder();
        int reminder;

        while (n > 0) {
            reminder = n % 3;
            n = n / 3;
            if (reminder == 0) {
                n--;
                reminder = 4;
            }
            answer.insert(0, reminder);
        }
        return answer.toString();
    }

    public static void main(String[] args) {
        NumberOf124World N = new NumberOf124World();
        System.out.println(N.solution(27));
    }
}
