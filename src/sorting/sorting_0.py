# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here

    # compare the first elements of each array
    for i in range(len(merged_arr)):
    # whichever is smaller, add to the merged_arr and pop from original
        if arrA[0] < arrB[0]:
            merged_arr.insert(i, arrA[0])
            arrA.pop(0)
        else:
            merged_arr.insert(i, arrB[0])
            arrB.pop(0)
    # compare the first elments again
    # if either is empty, add remaining elements in other array


    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here

    # divide given arr into lists of elements
    n = 1
    lists = [arr[i * n:(i + 1) * n] for i in range((len(arr) + n - 1) // n )]  
    print(lists)

    # take sequential pairs of lists
    # list comprehension
    # lists = [[lists[idx][0], lists[idx + 1][0]].sort()] for idx in range(0, len(lists), 2)]  
    # print(lists) 

    lists2 = []
    print("LEN: ", len(lists))
    x = 0
    if len(lists) % 2 != 0:
        x = len(lists) - 1
    else:
        x = len(lists)

    for idx in range(0, x, 2):
        print("IDX: ", idx)
        # compare first indexes
        
        to_sort = [lists[idx][0], lists[idx + 1][0]]
        to_sort.sort()
        lists2.append(to_sort)
        # if lists[idx][0] < lists[idx + 1][0]:


    merge_sort(lists2)
            
            # append lower value
            # repeat until until pairs are completely appended
    



    return lists2

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

