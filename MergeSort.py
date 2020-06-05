# Implement Merge Sort
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
    "data9" : [1,1]     #failed on IK for some reason
}


#-----------------------------------------------------------------------------#
#                        MERGE  SORTING                                  
#-----------------------------------------------------------------------------#
def merge_sort(data):
    #checking if length is 1 then dont proceed ahead
    # length = len(data)
    # the checlk for length <=1 causes timeouts for some reason on bug datasets
    # if length <= 1:
    #     return
    # call the mergesort_helper for the entire array
    mergesort_helper(data,0,len(data)-1)

    return data

def mergesort_helper(data,start,end):
    if start >= end:
        return
    # Calculate the mid of the array So we can divide  the array
    aux = []
    mid = int((start + end)/2)
    # Call mergesort_helper for the left side of the array recursively
    mergesort_helper(data,start,mid)
    # Call mergesort_helper for the right side of the array recursively
    mergesort_helper(data,mid+1,end)
    i = start
    j = mid+1
    # this while loop is used to compare the elements on the left and right arrays
    # which ever element is smaller gets appended to the aux array
    # Here we compare elemetns accros left and righ and merge it 
    # as soon as one of the conditions is met elements in left or right are exhausted
    # The 2nd while loop will take care of the remeaining elements in the larger array
    while i <= mid and j <= end: # ensure i doesnt go beyond mid and j doesnt go beyond end
        if data[i] <= data[j]:
            aux.append(data[i])
            i += 1
        else:
            aux.append(data[j])
            j += 1

    # After the above while loop is finished either i or j have reached their end
    # it has finished the merging aspect of the function
    # now the remaining elements in the leftover array should be copied to aux
    while i <= mid:
        aux.append(data[i])
        i += 1
    while j <= end:
        aux.append(data[j])
        j += 1
    data[start:end+1] = aux
    return 
    

if __name__ == "__main__":
    # Call the dataset to test Bubble sort
    for i in range(len(data)):
        start_time = time.time()
        aux = merge_sort(data["data"+str(i+1)])
        print(aux)
        print("Merge time for data" + str(i+1) + " = "+ str(time.time() - start_time))