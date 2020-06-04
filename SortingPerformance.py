# Here we test the performance of each of the sorting algorithms
# data7 is the big sorted array which will test the efficiency

# import time to measure performance and respective sort implementations
import time
#Brute force sorting
import BubbleSort
import SelectionSort
# decrease and conq
import InsertionSort
# divide and conq
import MergeSort


# we have a data set starting with the very basic happy path to complex
data = {
    "data1" : range(10000)  #Large sorted array
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


#-----------------------------------------------------------------------------#
#                  DECREASE AND CONQUER                                  #
#-----------------------------------------------------------------------------#

    #                        INSERTION SORTING      
for i in range(len(data)):
    # invoke the start time to measure the performance
    start_time = time.time()
    # Calling bubble_sort for each data set
    InsertionSort.insertion_sort_iterative(data["data"+str(i+1)])
    print("Insertion time for data" + str(i+1) + " = "+ str(time.time() - start_time))

#-----------------------------------------------------------------------------#
#                        DIVIDE AND CONQ SORTING                         #
#-----------------------------------------------------------------------------#

#                        MERGE SORTING              
for i in range(len(data)):
    # invoke the start time to measure the performance
    start_time = time.time()
    # Calling bubble_sort for each data set
    MergeSort.merge_sort(data["data"+str(i+1)])
    print("Merge time for data" + str(i+1) + " = "+ str(time.time() - start_time))