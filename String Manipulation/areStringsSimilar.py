class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1.split(' ')
        s2 = sentence2.split(' ')

        # Logic: Simplest yet effective, String matching

        '''
            There's nothing in this question really, No deque, No two pointers, No bs needed

            Let's keep it simple, We split the two strings at whitespaces to get words

            Then we equate the starting and the ending words

            If they are same, we pop them

            Now those are gone, While loop checks for the next pairs

            If everything is gone from s1 i.e smaller string, This means that the middle part of s2 is now the missing part and it can be appended in s2 anytime to get the bigger string, So they are indeed similar

            However, If a mismatch is found, Then The strings can never be similar

            Eg. 
            sentence1 = "qbaVXO Msgr aEWD v ekcb"
            sentence2 = "Msgr aEWD ekcb"

            Here we find last words same, We remove them
            After that nothing is similar, This means that the missing words in the smaller sentence are not together and can never be inserted so as to make the bigger string out of the smaller one
            ** But why are we emphasizing over putting these words together instead of separately?
                The question says Two sentences sentence1 and sentence2 are similar if it is possible to insert an              "arbitrary sentence"
        
        That's it, :coinflipper: ;)
        '''

        if len(s1)>len(s2):
            s1 , s2 = s2 , s1 # s1 is the smaller always for ease of cases

        while(s1): # s1 becomes false when all elements of s1 are popped out, meaning both strings are similar
            if s2[0] == s1[0]: # First elements same
                s1.pop(0)
                s2.pop(0)
            elif s2[-1] == s1[-1]: # Last elements same
                s1.pop(-1)
                s2.pop(-1)
            else: # Nothing same and can be popped, Strings can never be similar, return False
                return False
        return True