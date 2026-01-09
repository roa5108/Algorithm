def solution(numbers, hand):
    answer = ''
    keypad = {
    1:(0,0), 2:(0,1), 3:(0,2),
    4:(1,0), 5:(1,1), 6:(1,2),
    7:(2,0), 8:(2,1), 9:(2,2),
    '*':(3,0), 0:(3,1), '#':(3,2)
    }
    
    left, right = keypad['*'], keypad['#']
    
    for n in numbers:
        if n in [1,4,7]:
            answer+='L'
            left = keypad[n]
            
        elif n in [3,6,9]:
            answer+='R'
            right = keypad[n]
            
        else:
            lx, ly = left
            rx, ry = right
            nx, ny = keypad[n]
            
            ldist = abs(lx - nx) + abs(ly - ny)
            rdist = abs(rx - nx) + abs(ry - ny)
            
            if ldist < rdist:
                answer+='L'
                left = keypad[n]
                
            elif ldist == rdist:
                if hand == 'right':
                    right = keypad[n]
                    answer+='R'
                else:
                    left = keypad[n]
                    answer+='L'
            else:
                answer+='R'
                right = keypad[n]
            
        
    return answer