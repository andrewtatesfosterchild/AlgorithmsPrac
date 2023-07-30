class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num = str(num)
        count = 0
        left, right = 0, 0

        while right < len(num):
            if (right - left + 1) < k:
                right += 1
            elif (right - left + 1) == k:
                s = num[left:right+1]
                n = int(s)
                
                if n != 0 and int(num) % n == 0:
                    count += 1

                left += 1
                right += 1

        return count
