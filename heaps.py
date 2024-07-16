def heapify(arr, idx):
    curr = idx

    L = 2*idx + 1
    R = 2*idx + 2
    
    if idx >= len(arr)//2:
        print(arr)
        return arr
        
    if arr[curr] < arr[L]:
        curr = L
    if arr[curr] < arr[R]:
        curr = R
    if curr != idx:
        parent_to_be = arr[curr]
        arr[curr] = arr[idx]
        arr[idx] = parent_to_be
        heapify(arr, curr)        
    return arr

a = [2,5,4,3,1,8,9,3,1,9,8]
heap = heapify(a, 4)
print(heap)
