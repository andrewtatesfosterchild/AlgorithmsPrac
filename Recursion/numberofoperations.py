class Solution:

    # Logic: Child's play recursion -_-

    '''
        For each operation, Add one and call the function again till you reach num = 0, Then return 0 which becomes your base case

        That's it, :coinflipper: ;)
    '''
    def stepcount(self,n,steps):
        if n == 0: # Base case
            return 0
        if n%2 == 0:
            return 1 + self.stepcount(n//2,steps) # Recursive call
        else:
            return 1 + self.stepcount(n-1,steps) # Recursive call

    def numberOfSteps(self, num: int) -> int:
        return self.stepcount(num,0)