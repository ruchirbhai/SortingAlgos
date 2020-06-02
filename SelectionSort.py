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
}


#-----------------------------------------------------------------------------#
#                        SELECTION  SORTING                                  
#-----------------------------------------------------------------------------#
def selection_sort(data):
    for i  in range(len(data)):
        min = i
        for j in range((len(data)-i)):
            if data[j+i] < data[min]:
                min = j + i
        data[i],data[min] = data[min],data[i]
    # print(data)

if __name__ == "__main__":
    # Call the dataset to test selection sort
    for i in range(len(data)):
        start_time = time.time()
        selection_sort(data["data"+str(i+1)])
        print("Selection time for data" + str(i+1) + " = "+ str(time.time() - start_time))
