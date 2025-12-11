# find max sum of subarray 
# input : [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# output : 6 

def find_max_sum(nums):
    curr_sum = 0 
    max_sum = 0 
    
    for num in nums:
        curr_sum += num 
        max_sum = max(max_sum,curr_sum)
        if curr_sum<0:
            curr_sum=0 
    return max_sum 

print(find_max_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

# find missing numbers 
# input: nums = [3, 0, 1]
# output : 2 

def find_missing(nums):
    n = len(nums)
    total = n*(n+1)//2 
    return total - sum(nums)

print(find_missing([3,0,1]))

# Two Sum 
# input: nums [2,7,11,15]
# target: 9 
# ouput : [0,1]

def two_sum(nums,target):
    seen = {} 
    pairs=[]
    for i,num in enumerate(nums):
        comp = target-num 
        if comp in seen:
            pairs.append((seen[comp],i))
        else:
            seen[num]=i 
    return pairs 

print(two_sum([2,7,11,15],9))

# sort an array 0s , 1s and 2s 
# input : nums = [2, 0, 2, 1, 1, 0]
# output: # nums becomes [0, 0, 1, 1, 2, 2] 

def sort_colors(nums):
    low,mid,high=0,0,len(nums)-1
    
    while mid<=high:
        if nums[mid]==0:
            nums[low],nums[mid]=nums[mid],nums[low]
            low+=1
            mid+=1
        elif nums[mid]==1:
            mid+=1
        else:
            nums[mid],nums[high]=nums[high],nums[mid]
            high-=1
            
    return nums
            

print(sort_colors([2, 0, 2, 1, 1, 0]))

# Find Duplicate Numbers 
# input: nums = [3, 1, 3, 4, 2]
# output: 3 

def find_duplicate(nums):
    slow,fast = nums[0],nums[0]
    
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow==fast:
            break 
    
    slow=nums[0]
    while slow!=fast:
        slow=nums[slow]
        fast = nums[fast]
    return slow 
    
print(find_duplicate([3, 1, 3, 4, 2]))

# merge two sorted array 
# nums1 = [1, 2, 3, 0, 0, 0]
# m = 3
# nums2 = [2, 5, 6]
# n = 3

def merge(nums1,nums2,m,n):
    i,j,k = m-1,n-1,m+n-1
    while i>=0 and j>=0:
        if nums1[i]>nums2[j]:
            nums1[k] = nums1[i]
            i-=1 
        else:
            nums1[k]=nums2[j]
            j-=1
        k-=1
    while j>=0:
        nums1[k]=nums2[j]
        j-=1
        k-=1
    return nums1
        

print(merge([1,2,3,0,0,0],[2,5,6],3,3))

# Find Majority ELement 
# nums = [3, 2, 3] output: 3 

def majority_element(nums):
    candidate,count=None,0 
    for num in nums:
        if count==0:
            candidate = num 
        count += (1 if num == candidate else -1)
    return candidate 
    
print(majority_element([3,2,3,1,0,4,4,4,4]))

# Best time to buy sell and stock 
# prices = [7,1,5,3,6,4]
# output: 5 
# # Explanation: Buy at price 1 and sell at price 6 (6 - 1 = 5)

def maxProfit(prices):
    min_price,max_profit=float('inf'),0 
    for price in prices:
        # find min price to buy stock  
        min_price = min(min_price,price)
        # find max price where max price 
        max_profit = max(max_profit,price-min_price)
    return max_profit 
    
print(maxProfit([7,1,5,3,6,4]))

# Find the Intersection of Two Arrays
# nums1 = [4, 9, 5]
# nums2 = [9, 4, 9, 8, 4]
# output : [9,4]

def intersection(nums1,nums2):
    return list(set(nums1) & set(nums2))
    
print(intersection([4, 9, 5],[9, 4, 9, 8, 4]))

#  Find the Longest Consecutive Sequence
# nums = [100, 4, 200, 1, 3, 2]
# output : Length: 4

def longestConsecutive(nums):
    num_set = set(nums)
    longest_streak=0
    for num in num_set:
        if num-1 not in num_set:
            current_num = num 
            current_streak = 1
            while current_num + 1 in num_set:
                current_num+=1
                current_streak+=1
                
            longest_streak=max(longest_streak,current_streak)
            
    return longest_streak
    
print(longestConsecutive([100, 4, 200, 1, 3, 2]))



