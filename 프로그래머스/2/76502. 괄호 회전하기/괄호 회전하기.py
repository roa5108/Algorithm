def solution(s):
    answer = 0
    doubleS = s*2
    
    for i in range(len(s)):
        rotated = doubleS[i:i+len(s)]
        if isRight(rotated):
            answer+=1
    return answer

def isRight(arr):
    st = []
    for i in arr:
        if i in "([{":
            st.append(i)
        else:
            if not st:
                return False
            if i==')' and st[-1]=='(':
                st.pop()
            if i==']' and st[-1]=='[':
                st.pop()
            if i=='}' and st[-1]=='{':
                st.pop()
    return False if st else True