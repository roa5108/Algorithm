class Solution {
    public int solution(int n) {
        int rest = 0;
        if (1<=(n%7) && (n%7) < 7) {
            rest = 1;
        }
        return n/7+rest;
    }
}