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
}


#-----------------------------------------------------------------------------#
#                        BUBBLE  SORTING                                  
#-----------------------------------------------------------------------------#
def bubble_sort(data):
    for i  in range(len(data) -1):
        for j in range((len(data) -1),i,-1):
            if data[j] < data[j-1]:
                data[j],data[j-1] = data[j-1],data[j]
        # print(data)
    # print(data)

if __name__ == "__main__":
    # Call the dataset to test Bubble sort
    for i in range(len(data)):
        start_time = time.time()
        bubble_sort(data["data"+str(i+1)])
        print("Bubble time for data" + str(i+1) + " = "+ str(time.time() - start_time))