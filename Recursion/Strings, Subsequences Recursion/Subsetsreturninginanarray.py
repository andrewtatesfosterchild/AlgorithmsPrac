 def helper (self , nums , processed):
        if nums == []:
            list = []
            list.append(processed)
            return list
        
        num = nums[0]

        left = self.helper(nums[1:] , processed + [num])
        right = self.helper(nums[1:] , processed)

        left.extend(right)

        return left

def subsets(self, nums):
    processed = []

    return self.helper(nums, processed)