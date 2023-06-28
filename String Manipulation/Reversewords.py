class Solution:
    def reverseWords(self, s: str) -> str:
        # Logic: bs question -_-

        '''
            Not explaining this
        '''
        
        s = s.strip().split()

        s = [x for x in s if x != '']

        return " ".join(list(reversed(s)))