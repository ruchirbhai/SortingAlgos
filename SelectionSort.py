# Implement Selection Sort
import time

# we have a data set starting with the very basic happy path to complex
data = {
    "data1" : [5,4,1,3,2],      # happy path easy to vizualize
    "data2" : [5,4,1999,3,2,8,7,6,10,100],     #larger range of values
    "data3" : [5,4,1,3,2,2],        # repeated values
    "data4" : [1,1,1,1,1,1],        # every element is the same
    "data5" : [0,22,100,1,2,3,4,5,6,7,7,8,89,9,0,-1],   #negative + zero
    "data6" : [5,4,3,2,1],      #reverse sorted array
    "data7" : [1],      # data with  one value
    "data8" : [],       # data with  NULL value
}


#-----------------------------------------------------------------------------#
#                        SELECTION  SORTING                                  
#-----------------------------------------------------------------------------#
def selection_sort(data):
    # start the for loop to iterate over the data
    # Struggled to figure out how to iterate with indices in python as i think i C/C++ terms
    for i  in range(len(data)):
        # In selection sort we go from left to right
        # Select the first index and NOT the value in the array and make it min
        min = i     # starts with i = 0 
        # Start the second loop which is of the length data - i
        # example data1 = [5,4,1,3,2] 
        # OutIter 1: range for i is 0 to 5
        # length 5, min = 0, range for j is 0 to 4
         # OutIter 2: i = 1
        # length 4, min = 1, range for j is 0 to 3       
        for j in range((len(data)-i)):
            # i = 0
            # InIter 1: data[0+0] < data[0] i.e. 5 < 5 false
            # InIter 2: data[1+0] < data[0] i.e. 4 < 5 True, so update min to 1 + 0
            # InIter 3: data[2+0] < data[1] i.e. 1 < 4 True, so update min to 2 + 0
            # InIter 4: data[3+0] < data[2] i.e. 3 < 1 false
            # InIter 5: data[4+0] < data[2] i.e. 2 < 1 false
            # i = 1, data = [1,4,5,3,2] 
            # InIter 1: data[0+1] < data[1] i.e. 4 < 4 false
            # InIter 2: data[1+1] < data[1] i.e. 5 < 4 false
            # InIter 3: data[2+1] < data[1] i.e. 3 < 4 True, so update min to 2 + 1
            # InIter 4: data[3+1] < data[3] i.e. 2 < 3 True, so update min to 3 + 1

            if data[j+i] < data[min]:
                min = j + i
        # OutIter 1: We get the min as 2 i.e. data[min] = 1 
            # Thus from the first scan we got the the minimum element 
            # Now swap the data[i] with data[min] i.e. data[0] with data[2] i.e. swap 5 with 1
            # After iteration 1 data = [1,4,5,3,2] 
        # OutIter 2: We get the min as 4 i.e. data[min] = 2 
            # Thus from the second scan we got the the minimum element 
            # Now swap the data[i] with data[min] i.e. data[1] with data[4] i.e. swap 4 with 2
            # After iteration 2 data = [1,2,5,3,4]
        # OutIter 3: min = 3 so result data = [1,2,3,5,4]
        # OutIter 4: min = 4 so result data = [1,2,3,4,5]
        data[i],data[min] = data[min],data[i]
    # print(data)

if __name__ == "__main__":
    # Call the dataset to test selection sort
    for i in range(len(data)):
        start_time = time.time()
        selection_sort(data["data"+str(i+1)])
        print("Selection time for data" + str(i+1) + " = "+ str(time.time() - start_time))
