class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # Logic: Very simple string manipulation

        '''
            Pick out the smallest word and set it as prefix
            We'll keep comparing each character of this prefix to the character of the words in strs and keep removing elements which do not match in each word, Thus prefix becomes shorter i.e. prefix = prefix[:i], each time and LCP is eventually obtained

            That's it
            :coinflipper: ;)
        '''
        prefix = min(strs, key=len)
        
        strs.remove(prefix)

        for words in strs:
            i = 0
            while i < len(prefix) and prefix[i] == words[i]:
                i+=1
            prefix = prefix[:i]

        return prefix

        