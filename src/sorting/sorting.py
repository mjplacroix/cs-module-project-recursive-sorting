# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = []

    # Your code here
    print(arrA, arrB)
    for i in range(elements):
    # whichever is smaller, add to the merged_arr and pop from original
        if len(arrA) == 0:
            merged_arr.extend(arrB)
        elif len(arrB) == 0:
            merged_arr.extend(arrA)
        elif arrA[0] < arrB[0]:
            merged_arr.append(arrA[0])
            arrA.pop(0)
        else:
            merged_arr.append(arrB[0])
            arrB.pop(0)
    print(merged_arr)


    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here

    # divide given arr into lists of elements
    lists = [arr[i:i+1] for i in range(len(arr))] 
    print("FULL: ", lists)
    arr2 = []

    # take sequential pairs of lists
    print("LEN1: ", len(lists))
    for idx in range(0, len(lists), 2):
        print("IDX: ", idx)
        # compare first indexes
        arr = merge(lists[idx], lists[idx + 1])
        arr2.append(arr)
        print(arr2)

    merge_sort(arr2)
    return arr

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

