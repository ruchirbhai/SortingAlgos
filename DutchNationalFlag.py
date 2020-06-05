balls = ["G", "B","G","G","R","B","R","G"]
    
def dutch_flag_sort_brute(balls):
    
    length = len(balls)
    if length <= 1:
        return
    
    rgb = {"R": 1, "G" : 2, "B" : 3}

    for i in range(length-1):
        j = i + 1 
        for j in range(j,0,-1):
            if rgb[balls[j]] < rgb[balls[j-1]]:
                balls[j],balls[j-1] = balls[j-1], balls[j]
            # if balls[i] == 'B':
            #     print(rgb[balls[i]])
                
    return balls
    
def dutch_flag_sort(balls):
    length = len(balls)
    if length <= 1:
        return

    left_ptr = 0
    curr_ptr = 0
    right_ptr = length -1

    while curr_ptr <= right_ptr:
        if balls[curr_ptr] == 'R':
            balls[curr_ptr],balls[left_ptr] = balls[left_ptr], balls[curr_ptr]
            curr_ptr += 1
            left_ptr += 1
        elif balls[curr_ptr] == 'G':
            curr_ptr+=1
        
        elif balls[curr_ptr] == 'B':
            balls[curr_ptr],balls[right_ptr] = balls[right_ptr], balls[curr_ptr]
            right_ptr -= 1
    
    print(balls)
    return balls
dutch_flag_sort(balls)