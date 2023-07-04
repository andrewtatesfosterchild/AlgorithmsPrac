# Defy your usual RBS with pivots, It wont work in recursion
# Here, 3 cases will do the job

def binarysearch(nums, s, e, target):
    if s > e:
        return -1
    
    mid = s + (e-s)//2

    if target == nums[mid]:
        return mid
    
    if nums[s] <= nums[mid]:
        if (target >= nums[s] and target <= nums[mid]):
            return binarysearch(nums , s , mid - 1, target)
        
        else:
            return binarysearch(nums , mid + 1, e, target)
        
    if target >= nums[mid] and target <= nums[e]:
        return binarysearch(nums , mid + 1 , e , target)
    else:
        return binarysearch(nums , s , mid - 1 , target)

        


def rotated_binary_search(nums, target):
    n = len(nums)
    return binarysearch(nums, 0, n - 1, target)

print(rotated_binary_search([2 , 3 , 4 , 1] , 4))
