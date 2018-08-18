# http://interactivepython.org/courselib/static/pythonds/SortSearch/toctree.html

class myData(object):
    def __init__(self, k, v):
        self.k, self.v = k, v

aList = [myData(1, 5), myData(1, 6)]

# O(n**2), O(n), O(n*log2(n))
def insert_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i
        while j > 0 and temp < arr[j-1]: # <=?
            arr[j] = arr[j-1]
            j = j-1
        arr[j] = temp
    return arr

# O(n**2), O(n**2)
def selection_sort(arr):
    for i in range(len(arr)-1):
        index = i
        for j in range(i, len(arr)):
            if arr[j] < arr[index]:
                index = j
        if index != i:
            arr[i], arr[index] = arr[index], arr[i]
    return arr

# O(n**2), O(n**2)/O(n)
def bubble_sort(arr):
    for i in range(len(arr)):
        found = False
        for j in range(1, len(arr)-i):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
                found = True
        if not found:
            break
    return arr

# O(nlog(n)), O(n**2)
def quick_sort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    if first<last:
        splitpoint = partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
    pivot = alist[first]
    l = first+1
    r = last
    
    done = False
    while not done:
        while l <= r and alist[l] <= pivot:
            l = l + 1
        while alist[r] >= pivot and r >= l:
            r = r - 1
        if r < l:
            done = True
        else:
            alist[l], alist[r] = alist[r], alist[l]
    alist[first], alist[r] = alist[r], alist[first]

    return r

# O(nlog(n)), O(nlog(n)), O(n)
def merge_sort(alist):
#     print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
#     print("Merging ",alist)

def shell_sort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist,startposition,sublistcount)
#             print("After increments of size", sublistcount,
#                   "The list is", alist)
        sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):
        currentvalue = alist[i]
        position = i
        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap
        alist[position]=currentvalue

# 堆构建
def build_heap(arr):
    length = len(arr)
    # 找到最后一个非叶子节点
    index = length//2 - 1
    # 从最后一个非节点开始依次向上做堆调整
    for i in range(index, -1, -1):
        heapify(arr, i)

# 堆调整，这里按大顶堆进行调整
def heapify(arr, index):
    # 叶子节点无须再做堆调整
    if index > len(arr)/2 - 1:
        return None
    max_index = index
    left_child_index = index*2 + 1
    right_child_index = index*2 + 2
    if left_child_index < len(arr) and arr[left_child_index] > arr[max_index]:
        max_index = left_child_index
    if right_child_index < len(arr) and arr[right_child_index] > arr[max_index]:
        max_index = right_child_index

    if arr[max_index] != arr[index]:
        temp = arr[max_index]
        arr[max_index] = arr[index]
        arr[index] = temp
        # 递归调整
        heapify(arr, max_index)

# 堆排序
def heap_sort(arr):
    arr_sorted = []
    # 先构建堆
    build_heap(arr)
    # 交换堆顶元素和堆末尾元素，交换后堆末尾元素为最大值元素
    while len(arr) != 0:
        temp = arr[0]
        arr[0] = arr[len(arr)-1]
        arr[len(arr)-1] = temp
        arr_sorted.insert(0, arr.pop(len(arr)-1))
        # 调整
        heapify(arr, 0)
    arr[:] = []
    arr.extend(arr_sorted)

if __name__ == '__main__':
    iterObj = [1, 9, 7, 3, 2, 0, 81, 9, 32, 2, 6]
    exp = [0, 1, 2, 2, 3, 6, 7, 9, 9, 32, 81]
    
    def _assertEqual(a, b, prefix):
        msg = 'pass'
        if a != b:
            msg = 'Error! %s != %s' % (a, b)
        print('[%s]: %s' % (prefix, msg))
        
    def _testAlgo(algo):
        arr = list(iterObj)
        algo(arr)
        _assertEqual(arr, exp, algo.__name__)
    
    selfMod = __import__(__name__)
    algoList = [v for k,v in selfMod.__dict__.items()
                if k.endswith('_sort') and callable(v)]
    list(map(_testAlgo, algoList))