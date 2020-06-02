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
    # start the for loop to iterate over the data
    # Here the range needs to reduce by 1 to match the indices... i think
    # data1 = [5,4,1,3,2] so i goes from 0 to 4
    for i  in range(len(data) -1):
        # The main difference with selection sort bubble sort goes from right to left
        # Struggled to figure out how to go in the reverse order in for loop
        # for reverse useage range(start,stop, step) 
        # Start is  (len(data) -1) i.e. 5-1 = 4
        # Stop is i which is  0,1,...
        # Step is -1 which means go reverse by 1 step 
        # So life of j is iter 1: 4,3,2,1,0, iter 2: 4,3,2,1 as i is now 1 and so on
        for j in range((len(data) -1),i,-1):
            # iter 1: i = 0 and j = 4, data[4] < data[4-1] i.e. 2<3, True so swap 
            # iter 2: i = 0 and j = 3, data[3] < data[3-1] i.e. 2<1, false 
            # iter 3: i = 0 and j = 2, data[2] < data[2-1] i.e. 1<4, True so swap 
            # iter 4: i = 0 and j = 1, data[1] < data[1-1] i.e. 1<5, True so swap 
            if data[j] < data[j-1]:
               # i = 0
                #Swap 1: [5,4,1,3,2]  --> [5,4,1,2,3] 
                #Swap 2: [5,4,1,2,3]  --> [5,1,4,2,3] 
                #Swap 3: [5,1,4,2,3]  --> [1,5,4,2,3] 
                # i = 1
                #Swap 4: [1,5,4,2,3]  --> [1,5,2,4,3] 
                #Swap 5: [1,5,2,4,3]  --> [1,2,5,4,3] 
                # i = 2
                #Swap 6: [1,2,5,4,3]  --> [1,2,5,3,4] 
                #Swap 7: [1,2,5,3,4]  --> [1,2,3,5,4]  
                # i = 3 
                # Swap 8: [1,2,3,5,4] --> [1,2,3,4,5]

                data[j],data[j-1] = data[j-1],data[j]
        # print(data)
    # print(data)

if __name__ == "__main__":
    # Call the dataset to test Bubble sort
    for i in range(len(data)):
        start_time = time.time()
        bubble_sort(data["data"+str(i+1)])
        print("Bubble time for data" + str(i+1) + " = "+ str(time.time() - start_time))