class Solution {
    public int findJudge(int n, int[][] trust) {
        int answer = -1;
        for(int i = 0; i < trust.length; i++){
             if(answer == -1){
                answer = trust[i][1];
            }
            else if(trust[i][1] != answer){
                return -1;
            }
        }
        return answer;
    }
}