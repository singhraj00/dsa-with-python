## Searching Algorithms 

## 1. Linear Search 
## a. not need to sorted array 
## b. brute force method 
## c. time complexity : o(n) 

def linear_search(arr,item):
    for i in range(len(arr)):
        if arr[i]==item:
            return i
    return -1 

print('------ linear search ------')   
print(linear_search([2,5,7,11],2))
print(linear_search([2,5,7,11],11)) 
print(linear_search([2,5,7,11],15))

## Binary Search 
## a. need sorted array 
## b. efficient than linear_search
## c. time complexity : o(log(n)) 

## 1. Using Recursion 
## 2. Using Loop 

def binary_search(arr,low,high,item):
    if low<=high:
        mid = (low + high) // 2 
        if arr[mid]==item:
            return mid 
        elif arr[mid]>item:
            return binary_search(arr,low,mid-1,item)
        else: 
            return binary_search(arr,low+1,high,item)
    return -1 

arr = [2,5,7,11]

print('---- Binary Search ------')
print(binary_search(arr,0,len(arr)-1,2))
print(binary_search(arr,0,len(arr)-1,11))
print(binary_search(arr,0,len(arr)-1,15))

## 2. Using Loop 

def binary_search_loop(arr,item):
    low, high = 0,len(arr)-1
    
    while low<=high:
        mid = (low+high)//2
        if arr[mid]==item:
            return mid 
        elif arr[mid]<item:
            low = mid + 1
        else:
            high = mid - 1 
    return -1 
    
print('---- Binary Search Loop ------')
print(binary_search_loop(arr,2))
print(binary_search_loop(arr,11))
print(binary_search_loop(arr,15))

## Sorting 

## write an program to check given array is sorted or not 

def is_sorted(arr):
    sorted = True 
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            sorted = False 
    return sorted 

print('----- Check Sorted Or Not -----')
print(is_sorted([2,5,7,11]))
print(is_sorted([5,2,11,7]))

## Sorting Algorithms 
## 1. Monkey Sort 
## 2. Sleep Sort 
## 3. Bubble Sort 
## 4. Selection Sort 
## 5. Merge Sort 

## 1. Monkey Sort
## a. time complexity - o(inf)
## 
import random 
import time 

def monkey_sort(arr):
    while not is_sorted(arr):
        time.sleep(1)
        random.shuffle(arr)
        print(arr)
    print(arr)
    
# monkey_sort([7,1,5,9])

## Sleep Sort 
## time complexity - O(n + Max(A))

import threading
import time

def sleep_sort(arr):
    def worker(x):
        time.sleep(x)   # har number x second ke liye wait karega
        print(x, end=" ")

    threads = []
    for num in arr:
        t = threading.Thread(target=worker, args=(num,))
        t.start()
        threads.append(t)

    # sab threads khatam hone tak wait karo
    for t in threads:
        t.join()

# Example
#arr = [6, 5, 2, 11]
#print("Input:", arr)
#print("Sorted output:", end=" ")

# sleep_sort(arr)

## Bubble Sort 
## Time Complexity Worst Case - O(n^2), Bast Case - O(n)
## Space Complexity - O(1)
## Stable - means if two values are same not chaging order during sorting. 
## Adaptive - means if given akready sorted algorithm it's take advantage and reduce time Complexity
## By nature bubble sort is not Adaptive but we can make it adaptive using flag concept .
## Bubble sort is stable because it's not change order if two items are equals 

## Code Implementation 
def bubble_sort(arr):
    for i in range(len(arr)-1):
        flag = 0
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                flag = 1
                
        if flag == 0:
            break 
            
    return arr
    
print('---- Bubble Sort ------')
print(bubble_sort([2,11,7,5,9]))

## Selection Sort 
## Time Complexity - O(n^2) Space Complexity - O(1)
## Adaptive - No , Stable - No 
## Benefits - Faster comparison than bubble sort (less number of swapping)

def selection_sort(arr):
    for i in range(len(arr)-1):
        min = i 
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min]:
                min = j
        arr[i],arr[min]=arr[min],arr[i]
        
    return arr 
    
print('---- Selection Sort ------')    
print(selection_sort([2,5,11,9,7]))

## Merge Sort 
## Time Conplexity - O(nlog(n))
## Space complexity - O(n)
## Adaptive - No
## Stable - Yes
 
def merged_sorted_array(arr1,arr2,arr):
    i=j=k=0
    
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            arr[k] = arr1[i]
            i+=1 
            k+=1 
        else:
            arr[k] = arr2[j]
            j+=1
            k+=1 
            
    # extend remaining elements 
    while i < len(arr1):
        arr[k] = arr1[i]
        i+=1
        k+=1
    while j < len(arr2):
        arr[k] = arr2[j]
        j+=1
        k+=1
    
    return 

def merge_sort(arr):
    
    if len(arr)==1:
        return arr 
        
    mid = len(arr)//2 
    
    left = arr[:mid]
    right = arr[mid:]
    
    merge_sort(left)
    merge_sort(right)
    
    merged_sorted_array(left,right,arr)
    
    return 

arr = [67, 57, 22, 69, 97, 33, 66]
merge_sort(arr)
print('****** Merge Sort *******')
print(arr)
