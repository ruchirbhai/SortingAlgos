import heapq

H = [21,1,45,78,3,55,5,5,0,5,]
# Use heapify to rearrange the elements
heapq.heapify(H)
print(H)
heapq.heappush(H,2)
print(H)