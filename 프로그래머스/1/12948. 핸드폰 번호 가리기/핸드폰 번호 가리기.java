class Solution {
    public String solution(String phone_number) {
        int len = phone_number.length();
        StringBuilder sb = new StringBuilder(phone_number);
        sb.replace(0, len-4, "*".repeat(len-4));
        return sb.toString();
    }
}