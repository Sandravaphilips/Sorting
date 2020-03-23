# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    merged_arr = []
    # TO-DO
    index_a = 0
    index_b = 0
    
    while index_a < len(arrA) and index_b < len(arrB):
        if arrA[index_a] < arrB[index_b]:
            merged_arr.append(arrA[index_a])
            index_a += 1
        else:
            merged_arr.append(arrB[index_b])
            index_b += 1

    while index_a < len(arrA):
        merged_arr.append(arrA[index_a])
        index_a += 1

    while index_b < len(arrB):
        merged_arr.append(arrB[index_b])
        index_b += 1

    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) == 0 or len(arr) == 1:
        return arr
    mid = int(len(arr)/2)
    lhs = []
    rhs = []

    for i in arr[:mid]:
        lhs.append(i)
    for i in arr[mid:]:
        rhs.append(i)  
    
    return merge(merge_sort(lhs), merge_sort(rhs))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO
    merged_arr = [0] * (end - start + 1)
    # TO-DO
    index = 0
    s = start
    m = mid+1
    
    if len(arr) == 0:
        return arr

    while s <= mid and m <= end:
        if arr[s] <= arr[m]:
            merged_arr[index] = arr[s]
            index += 1
            s += 1
        else:
            merged_arr[index] = arr[m]
            m += 1
            index += 1

    while s <= mid:
        merged_arr[index] = arr[s]
        index += 1
        s += 1
		
    while m <= end:
        merged_arr[index] = arr[m]
        index += 1
        m += 1

    for i in range(start, end+1):
        arr[i] = merged_arr[i - start]
    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO
    if len(arr) == 0 or len(arr) == 1:
        return arr
    if l < r:
        mid = int((l+r)/2)
        merge_sort_in_place(arr, l, mid)  
        merge_sort_in_place(arr, mid+1, r) 
    
        return merge_in_place(arr, l, mid, r)
    

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
