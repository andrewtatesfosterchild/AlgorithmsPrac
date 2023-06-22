
# Sorting logic uses binarysearch to determine if an array is sorted or not
# log(N) instead of N
def isSorted(nums, s, e):
    if s >= e:
        return True

    mid = s + (e - s) // 2

    if nums[mid] > nums[mid + 1]:
        return False

    return isSorted(nums, s, mid) and isSorted(nums, mid + 1, e) # Applying binary search recursively on both parts

nums = [3, 3 , 3 , 4 , 3]
print(isSorted(nums, 0, len(nums) - 1))
