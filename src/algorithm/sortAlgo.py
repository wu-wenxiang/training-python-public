# http://interactivepython.org/courselib/static/pythonds/SortSearch/toctree.html

# O(n**2), O(n)
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
#         found = False
        for j in range(1, len(arr)-i):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
#                 found = True
#         if not found:
#             break
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
    pivotvalue = alist[first]
    leftmark = first+1
    rightmark = last
    
    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1
        if rightmark < leftmark:
            done = True
        else:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]
    alist[first], alist[rightmark] = alist[rightmark], alist[first]

    return rightmark

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