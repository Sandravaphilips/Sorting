# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
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

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(merge_sort(arr1))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO
    
    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
