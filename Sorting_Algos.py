import time
import threading

#   Bubble Sort
def bubbleSort(data, drawData, delay):
    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j]>data[j+1]:
                data[j],data[j+1]=data[j+1],data[j]
                drawData(data, ['green' if x==j or x==j+1 else 'red' for x in range(len(data))])
                threading.Thread(target = time.sleep(delay)).start

#   Quick Sort
def partition(data, head, tail, drawData, delay):
    border = head
    pivot = data[tail]

    drawData(data, getColourArray(len(data), head, tail, border, border))
    time.sleep(delay)

    for j in range(head, tail):
        if data[j]<=pivot:
            drawData(data, getColourArray(len(data), head, tail, border, j, True))
            time.sleep(delay)
            
            data[border], data[j]=data[j], data[border]
            border += 1
        drawData(data, getColourArray(len(data), head, tail, border, j))
        time.sleep(delay)
    
    drawData(data, getColourArray(len(data), head, tail, border, tail, True))
    time.sleep(delay)

    data[border], data[tail] = data[tail], data[border]
    return border

def quickSort(data, head, tail, drawData, delay):
    if head < tail :    
        partitionIdx = partition(data, head, tail, drawData, delay)
        
        #left Partition
        quickSort(data, head, partitionIdx-1, drawData, delay)

        #Right Partition
        quickSort(data, partitionIdx, tail, drawData, delay)

def getColourArray(dataLen, head, tail, border, currIdx, isSwapping = False):
    colourArray = []
    for  i in range(dataLen):
        #base colour
        if i>=head and i<= tail:
            colourArray.append('gray')
        else:
            colourArray.append('White')

        if i==tail:
            colourArray[i]='blue'
        elif i==border:
            colourArray[i]='red'
        elif i==currIdx:
            colourArray[i]='yellow'

        if isSwapping:
            if i == border or i == currIdx:
                colourArray[i]='orange'

    return colourArray

#    Selection Sort
def selectionSort(list, drawData, delay):
    for i in range(len(list)-1):
        min=i
        for j in range (i,len(list)):
            if list[j]<list[min]:
                    min=j
                    
        list[i], list[min] = list[min], list[i]
        drawData(list, ['green' if x==i or x==min else 'red' for x in range(len(list))])
        time.sleep(delay)

#   Merge Sort
def mergeSort(data, drawData, delay):
    merge_sort_algo(data, 0, len(data)-1, drawData, delay)

def merge_sort_algo(data, left, right, drawData, delay):
    if left < right:
        middle = (left + right) // 2
        merge_sort_algo(data, left, middle, drawData, delay)
        merge_sort_algo(data, middle + 1, right, drawData, delay)
        merge(data, left, middle, right, drawData, delay)

def merge(data, left, middle, right, drawData, delay):
    drawData(data, getPaintArray(len(data), left, middle, right))
    time.sleep(delay)

    leftPart = data[left : middle + 1]
    rightPart = data[middle + 1:right + 1]
    
    leftIdx = rightIdx = 0

    for dataIdx in range(left, right + 1):
        if leftIdx < len(leftPart) and rightIdx < len(rightPart):
            if leftPart[leftIdx] <= rightPart[rightIdx]:
                data[dataIdx] = leftPart[leftIdx]
                leftIdx += 1
            else:
                data[dataIdx] = rightPart[rightIdx]
                rightIdx += 1
        elif leftIdx < len(leftPart):
            data[dataIdx] = leftPart[leftIdx]
            leftIdx += 1
        else:
            data[dataIdx] = rightPart[rightIdx]
            rightIdx += 1

    drawData(data, ["green" if x>= left and x<= right else "white" for x in range (len(data))])
    time.sleep(delay)

def getPaintArray(length, left, middle, right):
    paintArray = []

    for i in range(length):
        if i >= left and i <= right:
            if i >= left and i <= middle:
                paintArray.append("yellow")
            else:
                paintArray.append("blue")
        else:
            paintArray.append("white")
    return paintArray