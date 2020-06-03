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
}


#-----------------------------------------------------------------------------#
#                        INSERTION  SORTING                                  
#-----------------------------------------------------------------------------#
def insertion_sort(data):
    # check is the data size is 1 then return true
    if len(data) <= 1:
        return
    
    # for a dataset greater than 1 go from 2 to end of array
    for i in range(0, (len(data) -1)):
        # get the new element so we can now insert this new element at the right place in the array
        new_element = data[i]
        # pointing j to the last value in the sorted part of the array, the left side 
        j = i + 1

        # Go from right to left as j keeps increasing from 1 to len(data) -1
        # Use the same logic as bubble sort here
        for j in range(j,0,-1):
            if data[j] < data[j-1]:
                data[j],data[j-1] = data[j-1],data[j]
            # print(data)
    # print(data)


if __name__ == "__main__":
    # Call the dataset to test Insertion sort
    for i in range(len(data)):
        start_time = time.time()
        insertion_sort(data["data"+str(i+1)])
        print("Insertion time for data" + str(i+1) + " = "+ str(time.time() - start_time))