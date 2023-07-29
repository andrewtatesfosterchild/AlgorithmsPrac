class Solution:
    # Logic: Two hashmaps?! With sliding window

    '''
        Two hashmaps and sliding , How will this work?

        For anagrams , Hashmaps are always used , Remember this.

        Besides this common information , We are supposed to maintain two hashmaps for this question

        One for the window, and other one for the substring

        siding the window through the string which maintaining a hashmap , We equate this hashmap with the substring map , If it is equal , We have an anagram , Else check the next window

        How do we do it though? Easy , Take a window initially of len(p) - 1 ,Make it a hashmap

        from len(p) - 1 to len(s) , Everytime you encounter an i , put it in the hashmap or increment its count , Then you equate both the hashmaps, If they are equal, It's an anagram and we append it

        If it is not , We slide the window by decreasing the hashmap's s[start] count by 1 , and a new element will be added and compared in the next loop

        This was an unique approach which performs sliding window on the string as well as the hashmap

        That's it , Easy , Cool
    '''
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        sdict = Counter(s[:len(p) - 1])
        pdict = Counter(p)
        start = 0

        res = []

        for i in range(len(p) - 1 , len(s)):
            sdict[s[i]]+=1

            if sdict == pdict:
                res.append(start)      

            sdict[s[start]] -=1

            if sdict[s[start]] == 0:
                del sdict[s[start]]

            start+=1
        
        return res
        