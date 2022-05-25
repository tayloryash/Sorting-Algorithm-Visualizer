# We need the time module to create some time difference between each comparison
import time

# Importing colors from colors.py
from colors import *

ascending = True
c1 = RED
c2 = [LIGHT_GREEN]
c3 = [BLUE]
c = 0

def bubble_sort(data, paintData, timeTick, ascending):
    size = len(data)
    global c
    for i in range(size - 1):
        for j in range(size - i - 1):
            if (data[j] > data[j + 1] and ascending) or (data[j] < data[j + 1] and not ascending):
                data[j], data[j + 1] = data[j + 1], data[j]
                c += 1
                paintData(data, [RED if x == j else LIGHT_GREEN if x == j + 1 else BLUE for x in range(len(data))],c)

                time.sleep(timeTick)

    paintData(data, [BLUE for x in range(len(data))],c)

def merge(data, start, mid, end, paintData, timeTick, ascending):
    global c
    p = start
    q = mid + 1
    tempArray = []

    for i in range(start, end + 1):
        if p > mid:
            tempArray.append(data[q])
            q += 1
        elif q > end:
            tempArray.append(data[p])
            p += 1
        elif ((data[p] < data[q] and ascending) or (data[p] > data[q] and not ascending)):
            tempArray.append(data[p])
            p += 1
            c+=1
        else:
            tempArray.append(data[q])
            q += 1

    for p in range(len(tempArray)):
        data[start] = tempArray[p]
        start += 1



def merge_sort(data, start, end, paintData, timeTick, ascending):
    global c

    if start < end:
        mid = int((start + end) / 2)
        merge_sort(data, start, mid, paintData, timeTick, ascending)
        merge_sort(data, mid + 1, end, paintData, timeTick, ascending)

        merge(data, start, mid, end, paintData, timeTick, ascending)

        paintData(data, [PURPLE if x >= start and x < mid else YELLOW if x == mid
        else DARK_BLUE if x > mid and x <= end else BLUE for x in range(len(data))],c)
        time.sleep(timeTick)

    paintData(data, [BLUE for x in range(len(data))],c)

def insertion_sort(data, paintData, timeTick, ascending):
    global c
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and ((key < data[j] and ascending) or (key > data[j] and not ascending)):
            data[j + 1] = data[j]
            c+=1
            j -= 1
            paintData(data, [RED if x == j else LIGHT_GREEN if x == j + 1 else BLUE for x in range(len(data))],c)
            time.sleep(timeTick)
        data[j + 1] = key
    paintData(data, [BLUE for x in range(len(data))],c)
def selection_sort(data, paintData, timeTick, ascending):
    global c
    for i in range(len(data)):

        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, len(data)):
            if (data[min_idx] > data[j] and ascending) or (data[min_idx] < data[j] and not ascending):
                min_idx = j
                c += 1

        # Swap the found minimum element with
        # the first element
        data[i], data[min_idx] = data[min_idx], data[i]

        paintData(data, [RED if x == i else LIGHT_GREEN if x == min_idx else BLUE for x in range(len(data))],c)
        time.sleep(timeTick)

    paintData(data, [BLUE for x in range(len(data))],c)


def partition(data,start, end, paintData, timeTick, ascending):
    global c
    i = (start - 1)
    pivot = data[end]  # pivot element

    for j in range(start, end):
        # If current element is smaller than or equal to the pivot
        if (data[j] <= pivot and ascending) or (data[j] >= pivot and not ascending):
            i = i + 1
            c+=1
            data[i], data[j] = data[j], data[i]


    data[i + 1], data[end] = data[end], data[i + 1]

    return (i + 1)


# function to implement quick sort
def quick( data,start, end, paintData, timeTick, ascending):  # a[] = array to be sorted, start = Starting index, end = Ending index

    if (start < end):
        p = partition(data, start, end,paintData, timeTick, ascending)# p is partitioning index
        paintData(data, [RED if x == p else LIGHT_GREEN if x == start else VIOLET if x == end else BLUE for x in range(len(data))], c)
        time.sleep(timeTick)
        quick(data, start, p - 1,paintData, timeTick, ascending)
        quick(data, p + 1, end,paintData, timeTick, ascending)
    paintData(data, [BLUE for x in range(len(data))], c)
