def solution(order):

    order = str(order)
    answer = 0
    for i in range(len(order)):
        if order[i] in '369':  
            answer+=1   
            
    return answer
