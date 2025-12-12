# Largest Element 

# Input: nums = [3, 3, 6, 1]

# Output: 6

# Explanation: The largest element in array is 6

def largest_element(nums):
    max_element = nums[0]
    for num in nums:
        if num>max_element:
            max_element=num 
    return max_element
    
print(largest_element([3,3,6,1]))

# check if the array is sorted 
def is_sorted(nums):
    for i in range(len(nums)-1):
        if nums[i]>nums[i+1]:
            return False 
    return True 
    
print(is_sorted([1,2,3,4]))
print(is_sorted([4,2,1,0]))

# second largest element without sorting 

def second_largest(nums):
    first=second=float('-inf')
    
    for num in nums:
        if num>first:
            second=first 
            first=num 
        elif first>num>second:
            second=num 
    
    if second==float('-inf'):
        return -1 
    
    return second 
 
print(second_largest( [8, 8, 7, 6, 5]))
print(second_largest([10, 10, 10, 10, 10]))  

# Linear Search 

def linear_search(nums,value):
    index=0
    for num in nums:
        if num==value:
            return index 
        index+=1 
    return -1


print(linear_search([2, 3, 4, 5, 3],3))
print(linear_search( [2, -4, 4, 0, 10],6)) 
print(linear_search([1,3,5,-4,1],1))

# Left Rotate Array By One 

def left_rotate_by_one(nums):
    if not nums:
        return 
    
    first = nums[0]
    n = len(nums)
    
    for i in range(1,n):
        nums[i-1]=nums[i]
    
    nums[-1] = first
    
    return nums

print(left_rotate_by_one([1,2,3,4,5]))    
print(left_rotate_by_one( [-1, 0, 3, 6]))

# Maximum Consecutive Ones

def max_cons_ones(nums):
    current_count = 0 
    max_count = 0 
    
    for num in nums:
        if num==1:
            current_count +=1 
            max_count = max(max_count,current_count)
        else:
            current_count = 0 
    return max_count
    
print(max_cons_ones( [1, 1, 0, 0, 1, 1, 1, 0]))
print(max_cons_ones([0, 0, 0, 0, 0, 0, 0, 0]))            
print(max_cons_ones([1, 0, 1, 1, 1, 0, 1, 1, 1]))

# move zeros to end 

def move_zeros(nums):
    left_non_zero=0 
    
    # step 1: move all non-zero to front 
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[left_non_zero] = nums[i]
            left_non_zero +=1 
    
    # step2 : fill the rest zeros 
    for i in  range(left_non_zero,len(nums)):
        nums[i]=0 
        
    return nums
        
print(move_zeros( [0, 1, 4, 0, 5, 2]))
print(move_zeros( [0, 0, 0, 1, 3, -2]))


# Left Rotate Array by K Places - O(n)

def left_rotate_k(nums,k):
    n = len(nums)
    if n==0:
        return 
    
    if not nums:
        return 
    if k<0:
        return False 
    
    k = k % n # handle k>n 
    
    nums[:] = nums[k:] + nums[:k]
    
    return nums 

print(left_rotate_k([1, 2, 3, 4, 5, 6],2))
print(left_rotate_k( [3, 4, 1, 5, 3, -5],8))

# better solution - O(1)

def reverse(nums,start,end):
    while start<end:
        nums[start],nums[end]=nums[end],nums[start]
        start+=1
        end-=1
        
def left_rotate(nums,k):
    n = len(nums)
    if n==0:
        return 
    
    k = k%n 
    
    # step 1 : reverse fikrst k element 
    reverse(nums,0,k-1)
    
    # step2 reverse rest of arrays
    reverse(nums,k,n-1)
    
    # reverse entirev array 
    reverse(nums,0,n-1)
    
    return nums

print(left_rotate([1, 2, 3, 4, 5, 6],2))
print(left_rotate( [3, 4, 1, 5, 3, -5],8))

# Remove Duplicates from sorted array 

def remove_duplicates(nums):
    if not nums:
        return 
    
    i=0  # pointer tp last unique element
    
    for j in range(1,len(nums)):
        if nums[j] !=  nums[i]:
            i+=1
            nums[i] = nums[j]
    
    return i+1,nums[:i+1]

print(remove_duplicates([0, 0, 3, 3, 5, 6]))
print(remove_duplicates([-2, 2, 4, 4, 4, 4, 5, 5]))

# Find Missing Number 

def find_missing(nums):
    n = len(nums)
    total = n*(n+1)//2 
    return total - sum(nums)

print(find_missing([0,2,3,1,4]))
print(find_missing([0,1,2,4,5,6]))

# Single Number - I 
def single_number(nums):
    result=0 
    for num in nums:
        result ^= num 
    return result 

print(single_number([1, 2, 2, 4, 3, 1, 4]))
print(single_number([5]))

# Union of Two Sorted Array 
def union_sorted_arrays(nums1,nums2):
    i=j=0 
    n,m = len(nums1),len(nums2)
    union = []
    
    while i<n and j<m:
        if nums1[i]<nums2[j]:
            if not union or union[-1] != nums1[i]:
                union.append(nums1[i])
            i+=1
        elif nums1[i]>nums2[j]:
            if not union or union[-1] != nums2[j]:
                union.append(nums2[j])
            j+=1 
        else:
            if not union or union[-1] != nums1[i]:
                union.append(nums1[i])
            i+=1 
            j+=1
    
    # add remaining element 
    while i<n:
        if union[-1] != nums1[i]:
            union.append(nums1[i])
        i+=1 
    
    while j<m:
        if union[-1] != nums2[j]:
            union.append(nums2[j])
        j+=1 
    
    return union 
    
print(union_sorted_arrays([3, 4, 6, 7, 9, 9],[1, 5, 7, 8, 8]))


# 2-Sum problem 
def two_sum(nums,target):
    hashmap={}
    for index,num in enumerate(nums):
        comp = target-num 
        if comp in hashmap:
            return [hashmap[comp],index]
        hashmap[num]=index 
    return -1 
    
print(two_sum([1,6,2,10,3],7))
print(two_sum([1, 3, 5, -7, 6, -3],0))

# search in a 2d matrix 

def search_matrix(mat,target):
    rows = len(mat)
    cols = len(mat[0])
    
    left = 0 
    right = rows*cols -1 
    
    while left<=right:
        mid = (left+right)//2 
        
        # convert mid to matrix cordinate 
        r = mid // cols 
        c = mid % cols 
        
        if mat[r][c] == target:
            return True 
        elif mat[r][c] <target:
            left = mid+1 
        else:
            right = mid -1 
    return -1 
    
print(search_matrix( [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ],8))
    

# Leaders in an Array 
# ⭐ "Leaders in an Array" Problem – Simple Explanation

# Leader ka matlab:
# Array me koi element tab leader hota hai jab uske right me jitne bhi elements hain, sab usse chhote ho.

# Aur rightmost element hamesha leader hota hai, kyunki uske right me koi element hota hi nahi.

def leaders(nums):
    n = len(nums)
    leaders_list = []
    
    max_right = nums[-1]
    leaders_list.append(max_right)
    
    for i in range(n-2,-1,-1):
        if nums[i]>max_right:
            leaders_list.append(nums[i])
            max_right = nums[i]
    
    leaders_list.reverse()
    return leaders_list 
    
print(leaders( [1, 2, 5, 3, 1, 2]))
print(leaders([-3, 4, 5, 1, -4, -5]))

# Print the matrix in spiral manner
# Input: matrix = [[1, 2, 3], [4 ,5 ,6], [7, 8, 9]]

# Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

# Explanation:

# The elements in the spiral order are 1, 2, 3 -> 6, 9 -> 8, 7 -> 4, 5


def spiral_order(mat):
    result = []
    
    top = 0 
    bottom = len(mat)-1
    left = 0 
    right = len(mat[0]) - 1 
    
    while top<=bottom and left<= right:
        # traverse left to right 
        for col in range(left,right+1):
            result.append(mat[top][col])
        top+=1 
        
        # traverse top to bottom 
        for row in range(top,bottom+1):
            result.append(mat[row][right])
        right -= 1
        
        # traverse right to left (if rows left)
        if top<=bottom:
            for col in range(right,left-1,-1):
                result.append(mat[bottom][col])
            bottom -=1 
        
        # traverse bottom to top (if columns left) 
        if left<=right:
            for row in range(bottom,top-1,-1):
                result.append(mat[row][left])
            left+=1 
    
    return result 
    
print(spiral_order( [[1, 2, 3], [4 ,5 ,6], [7, 8, 9]]))

# rotate matrix by 90 degree 
# step 1 transpose the matrix 
# step 2 reverse each row 

def rotate_90(matrix):
    n = len(matrix)
    
    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        
    for i in range(n):
        matrix[i].reverse()
    
    return matrix 
    
print(rotate_90( [[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(rotate_90( [[0, 1, 1, 2], [2, 0, 3, 1], [4, 5, 0, 5], [5, 6, 7, 0]]))

# Best time to buy and sell stock 

def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        min_price = min(min_price,price)
        max_profit = max(max_profit,price-min_price)
    
    return max_profit 
    
print(maxProfit([10, 7, 5, 8, 11, 9]))
print(maxProfit([5, 4, 3, 2, 1]))
print(maxProfit( [3, 8, 1, 4, 6, 2]))

# Rearrange array elements by sign
# Input : nums = [2, 4, 5, -1, -3, -4]
# Output : [2, -1, 4, -3, 5, -4]
#The positive number 2, 4, 5 maintain their relative positions and -1, -3, -4 maintain their relative positions

def RearrangebySign(nums):
    pos=[]
    neg=[]
    
    # step 1 separate positive and negatives 
    for x in nums:
        if x>0:
            pos.append(x)
        else:
            neg.append(x)
    
    # step 2 : build result 
    result = []
    i=j=0 
    
    while i<len(pos) and j<len(neg):
        result.append(pos[i])
        result.append(neg[j])
        i+=1 
        j+=1 
    
    return result 
    
print(RearrangebySign( [2, 4, 5, -1, -3, -4]))
print(RearrangebySign([1, -1, -3, -4, 2, 3]))
print(RearrangebySign( [-4, 4, -4, 4, -4, 4]))

# Find Duplicate Number (n+1) integers 

def find_duplicates(nums):
    # phase 1 : detect cycle 
    slow = nums[0]
    fast = nums[0]
    
    while True:
        slow=nums[slow]
        fast = nums[nums[fast]]
        if slow==fast:
            break 
    
    # phase 2 : find start cycle (duplicate)
    slow = nums[0]
    while slow!=fast:
        slow=nums[slow]
        fast = nums[fast]
        
    return slow 
    
print(find_duplicates([1,3,4,2,2]))
print(find_duplicates( [3,1,3,4,2]))

# Kadane's Algorithm (find the subarray with the largest sum and return the sum of the elements)

def max_sum_subarray(nums):
    current_sum=0 
    max_sum = nums[0]
    
    for num in nums:
        current_sum += num 
        max_sum = max(max_sum,current_sum)
        if current_sum<0:
            current_sum = 0 
    return max_sum
    
print(max_sum_subarray([2, 3, 5, -2, 7, -4]))
print(max_sum_subarray([-2, -3, -7, -2, -10, -4]))

# Grid Unique Path 

def uniquePaths(m, n):
    import math
    return math.comb(m + n - 2, m - 1)

print(uniquePaths(m=3,n=2))

# Sort an array of 0's 1's and 2's (skip already do)

# Pascal's Triangle 

# Generate Full Pascal Triangle
def generate_pascal(n):
    triangle=[]
    
    for i in range(n):
        row = [1] * (i+1) 
        for j in range(1,i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle 
    
print(generate_pascal(5))

# Print ONLY the Nᵗʰ Row of Pascal’s Triangle 

def nth_row(n):
    row = [1]
    val = 1 
    for k in range(1,n+1):
        val = val * (n-k+1) // k
        row.append(val)
    return row 

print(nth_row(3))

# Print ONLY One Element (nCk) 

def nck(n,k):
    if k>n-k:
        k = n-k 
    val=1 
    for i in range(k):
        val = val * (n-i) // (i+1)
    return val 
    
print(nck(3,3))
    

