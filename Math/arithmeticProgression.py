class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
          # Logic: Nerdy math approach

        '''
            Learn math kids -_-
        '''
        
        if len(arr) == 2:
            return True
        
        else:
            arr = sorted(arr)
            diff = arr[1] - arr[0]

            for i in range(len(arr)-1):
                if arr[i] + diff != arr[i+1]:
                    return False
        return True