class Solution1 {
    public long solution(long n) {
        long answer = -1;
        for(long i = 1; i <= Math.sqrt(n); i++) {
            if(i * i == n) {
                answer = i;
                break;
            }
        }
        return answer;
    }
}