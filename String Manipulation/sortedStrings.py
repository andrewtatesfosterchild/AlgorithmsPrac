class Solution:
    def sortSentence(self, s: str) -> str:
        # Logic: two / three passes, sorting not needed
        '''
            split at whitespace
            mantain a count of words appended
            use a while loop till all words not appended
            look for the next word to append (if int(strings[i][-1]) == words+1:)
            i+=1
            append when found res = res + ' ' + strings[i][:-1]
            i = i%len(strings) makes i go circular for the next pass
            return the res with lstrip (first word gets added after a whitespace)
            That's it :coinflipper: ;)
        '''
        strings = s.split(' ')
        words = 0
        res = ""
        i = 0

        while words<len(strings):
            if int(strings[i][-1]) == words+1:
                res = res + ' ' + strings[i][:-1]
                words+=1
            i+=1
            i = i%len(strings)
        
        return res.lstrip()
            
