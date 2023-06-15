class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        res = ""
        token = 0

        # Logic: Two pointers

        '''
            Self explainatory bs -_-
        '''

        while 1:
            print (token)
            if token == 0:
                if i < len(word1):
                    res = res + word1[i]
                    i+=1
                if j < len(word2):
                    token = 1
            else:
                if j < len(word2):
                    res = res + word2[j]
                    j+=1
                if i < len(word1):
                    token = 0

            if len(res) == len(word1+word2):
                break

        return res

