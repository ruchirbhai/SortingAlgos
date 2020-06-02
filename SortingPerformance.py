# Here we test the performance of each of the sorting algorithms
# data7 is the big sorted array which will test the efficiency

# import time to measure performance and respective sort implementations
import time
#Brute force sorting
import BubbleSort
import SelectionSort

# we have a data set starting with the very basic happy path to complex
data = {
    "data1" : [5,4,1,3,2],      # happy path easy to vizualize
    "data2" : [5,4,1999,3,2,8,7,6,10,100],     #larger range of values
    "data3" : [5,4,1,3,2,2],        # repeated values
    "data4" : [1,1,1,1,1,1],        # every element is the same
    "data5" : [0,22,100,1,2,3,4,5,6,7,7,8,89,9,0,-1],   #negative + zero
    "data6" : [5,4,3,2,1],      #reverse sorted array
    "data7" : range(10000)  #Large sorted array
}

#-----------------------------------------------------------------------------#
#                        BRUTE FORCE SORTING                                  #
#-----------------------------------------------------------------------------#

#                        SELECTION SORTING                                      

for i in range(len(data)):
    # invoke the start time to measure the performance
    start_time = time.time()
    # Calling selection_sort for each data set
    SelectionSort.selection_sort(data["data"+str(i+1)])
    print("Selection time for data" + str(i+1) + " = "+ str(time.time() - start_time))


    #                        BUBBLE SORTING      
for i in range(len(data)):
    # invoke the start time to measure the performance
    start_time = time.time()
    # Calling bubble_sort for each data set
    BubbleSort.bubble_sort(data["data"+str(i+1)])
    print("Bubble time for data" + str(i+1) + " = "+ str(time.time() - start_time))
