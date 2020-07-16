# Implement Bubble Sort
import time

# we have a data set starting with the very basic happy path to complex
data = {
    "data1" : [5,4,1,3,2],      # happy path easy to vizualize
    "data2" : [5,4,1999,3,2,8,7,6,10,100],     #larger range of values
    "data3" : [5,4,1,3,2,2],        # repeated values
    "data4" : [1,1,1,1,1,1],        # every element is the same
    "data5" : [0,22,100,1,2,3,4,5,6,7,7,8,89,9,0,-1],   #negative + zero
    "data6" : [5,4,3,2,1],      #reverse sorted array
    "data7" : [1],      # data with only 1 value
    "data8" : [],       # data with  NULL value
    "data9" : [4,2,1,6,2,10,4,3,10,6,5,6,7,2,10,10,4,6,5,8],
}


#-----------------------------------------------------------------------------#
#                        INSERTION  SORTING                                  
#-----------------------------------------------------------------------------#
def top_k(arr, k):
    result = []
    # for left_ptr in range(len(arr)-1):
    #     # result_dict[arr[left_ptr]] = 1
    #     curr_ptr = left_ptr + 1
    #     # go backwards in the array 
    #     for curr_ptr in range(curr_ptr,0,-1):
    #         # if arr[curr_ptr] > arr[curr_ptr - 1] and arr[curr_ptr] not in arr[:curr_ptr]:
    #         if arr[curr_ptr] > arr[curr_ptr - 1]:
    #             arr[curr_ptr], arr[curr_ptr - 1] = arr[curr_ptr - 1], arr[curr_ptr]
    
    arr.sort(reverse = True)
    ptr = 0
    while len(result) < k and ptr < len(arr):
        if(ptr == 0 or arr[ptr] != arr[ptr-1]):
            result.append(arr[ptr])
        ptr += 1
    return result


if __name__ == "__main__":
    # Call the dataset to test Insertion sort
    k = 4
    for i in range(len(data)):
        start_time = time.time()
        print(top_k(data["data"+str(i+1)],k))
        print("Insertion time for data" + str(i+1) + " = "+ str(time.time() - start_time))