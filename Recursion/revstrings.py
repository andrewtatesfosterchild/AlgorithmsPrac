class Solution:

    # Logic: What a drag -_-
    
    def reverse(self, l , r , s):
        if l>=r:
            return
        s[l],s[r] = s[r],s[l]
        self.reverse(l+1, r-1, s)

    def reverseString(self, s: List[str]) -> None:
        self.reverse(0, len(s)-1, s)

    