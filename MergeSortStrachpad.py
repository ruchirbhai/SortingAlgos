import time

arr = {
    "data1" : [5,4,1,3,2],      # happy path easy to vizualize
    "data2" : [5,4,1999,3,2,8,7,6,10,100],     #larger range of values
    "data3" : [5,4,1,3,2,2],        # repeated values
    "data4" : [1,1,1,1,1,1],        # every element is the same
    "data5" : [0,22,100,1,2,3,4,5,6,7,7,8,89,9,0,-1],   #negative + zero
    "data6" : [5,4,3,2,1],      #reverse sorted array
    "data7" : [1],      # data with only 1 value
    "data8" : [],       # data with  NULL value
    "data9" : [1,1]     #failed on IK for some reason
}


def merge_sort(arr):
    # Write your code here
    if len(arr) <= 1:
        return
    
    def helper(start, end, arr):
        # Base case If start > end
        if start >= end:
            return
        
        #calulate Mid
        mid = int((start+end)/2)
        
        #Left side of the array
        helper(start, mid, arr)
        
        #right side of the array
        helper(mid+1, end, arr)
        
        aux = []
        left_ptr, right_ptr = start, mid+1
        
        # This is for the comparision and merging
        while left_ptr <= mid and right_ptr <= end:
            if arr[left_ptr] < arr[right_ptr]:
                aux.append(arr[left_ptr])
                left_ptr += 1
            else: # right_ptr is greater
                aux.append(arr[right_ptr])
                right_ptr += 1
        # The leftover values need to be appended
        while left_ptr <= mid:
            aux.append(arr[left_ptr])
            left_ptr +=1
        
        while right_ptr <=end:
            aux.append(arr[right_ptr])
            right_ptr += 1
        
        arr[start:end+1] = aux
        return
    
    helper(0, len(arr)-1, arr)
    
    return arr

if __name__ == "__main__":
    # Call the dataset to test Bubble sort
    for i in range(len(arr)):
        start_time = time.time()
        aux = merge_sort(arr["data"+str(i+1)])
        print(aux)
        print("Merge time for data" + str(i+1) + " = "+ str(time.time() - start_time))