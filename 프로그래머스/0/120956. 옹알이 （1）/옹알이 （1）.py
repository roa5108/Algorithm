def solution(babbling):
    result=0
    arr = ["aya", "ye", "woo", "ma"]
    for b in babbling:
        for i in range(4):
            for word in arr:
                if word in b and b.startswith(word):
                    b = b.replace(word, "")
        print(b)
        if b=="":
            result+=1
            
    return result