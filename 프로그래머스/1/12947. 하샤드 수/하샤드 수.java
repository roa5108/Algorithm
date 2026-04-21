class Solution {
    public boolean solution(int x) {
        String word = String.valueOf(x);
        int tmp = 0;
        
        for (int i=0; i<word.length(); i++) {
            tmp+=word.charAt(i)-'0';
        }
        
        if (x%tmp==0) return true;
        else return false;
    }
} 