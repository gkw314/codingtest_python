def solution(hp):
    atk_5 = hp // 5
    hp = hp % 5
    
    atk_3 = hp // 3
    hp = hp % 3
    
    atk_1 = hp
        
            
    return atk_5 + atk_3 + atk_1