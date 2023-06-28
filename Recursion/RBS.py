def helper(nums, s, e):
    pivot = 0
    while s < e:
        mid = s + (e - s) // 2

        if mid > s and nums[mid - 1] > nums[mid]:
            pivot = mid - 1
            break
        elif mid < e and nums[mid] > nums[mid + 1]:
            pivot = mid
            break
        elif nums[s] < nums[mid]:
            s = mid + 1
        elif nums[s] >= nums[mid]:
            e = mid
    return pivot


def binarysearch(nums, s, e, target, pivot):
    if s > e:
        return -1

    mid = s + (e - s) // 2

    if target == nums[mid]:
        return mid
    elif target > nums[mid]:
        if mid + 1 >= pivot:
            return binarysearch(nums, pivot, e, target, pivot)
        else:
            return binarysearch(nums, mid + 1, pivot, target, pivot)
    else:
        return binarysearch(nums, s, pivot - 1, target, pivot)


def rotated_binary_search(nums, target):
    n = len(nums)
    pivot = helper(nums, 0, n - 1)
    return binarysearch(nums, 0, n - 1, target, pivot)

print(rotated_binary_search([2 , 3 , 4 , 1] , 1))
