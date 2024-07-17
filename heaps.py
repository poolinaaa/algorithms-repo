def heapify(arr, idx):
    curr = idx

    L = 2*idx + 1
    R = 2*idx + 2

    if idx >= len(arr)//2:
        return arr

    if arr[curr] < arr[L]:
        curr = L
    if R<len(arr):
        if arr[curr] < arr[R]:
            curr = R
    if curr != idx:
        parent_to_be = arr[curr]
        arr[curr] = arr[idx]
        arr[idx] = parent_to_be
        heapify(arr, curr)
    return arr


def build_heap(arr):
    i = 0
    while (len(arr)//2)-i >= 0:
        arr = heapify(arr, (len(arr)//2)-i)
        i += 1
    return arr

def del_node(arr, idx):
    arr[idx]=arr.pop()
    return heapify(arr,idx)

def insert_node(arr, value):
    arr.append(value)
    i = len(arr)-1
    while i > 0:
        parent = (i-1)//2
        if arr[parent]<arr[i]:
            temp = arr[parent]
            arr[parent]= arr[i]
            arr[i]=temp
            i=parent
        else:
            return arr
    return arr

a = [2, 5, 4, 3, 1, 8, 9, 3, 1, 9, 8]
heap = build_heap(a)
print(heap)
delated  = del_node(heap, 7)
print(delated)
delated  = del_node(heap, 4)
print(delated)
af = insert_node(heap, 16)
print(af)