class Solution:
    def printVertically(self, s: str) -> List[str]:
        final = []

        # Logic: string split
        '''
            The question is elegant
            It asks us to return the text as if it was printed vertically
            So what's the first instinctive thought? Look for whitespaces!

            Let's to that:
            Firstly, split the text and store it somewhere
            s = s.split()

            Now we need a max length variable for recording the word with maximum length in our s list above
            * Why do we need this?
                Because we want to print all characters in every word and there's only one way of doing that, Know what the meximum number of charaters possibel in a word are, And then you will not skip any character

            maxx = max(len(x) for x in s) # Just finding the max length, good ol' good ol'

            Cool, What next?

            lets start looping through maxx:
                initialize a string where the result will be stored temporarily

                Now we'll starting jumping through words:

                There's two cases you must understand now

                if i>=len(x):
                    This means that the current position in maxx is not present in current word, meaning that the word is over or the word will be over in the next iteration of i

                    So, start appending whitespaces for these kind of words
                    res = res + ' '
                
                else:
                    Here, The word still has some characters left, so append those characters, res = res + str(x[i])

                After every round of for x in s, A word will be generated which is the vertical form of print statement for the given statement, We simply append this word to the
                final list at the end of every i's round

                Then, A new round starts, res is resetted to a blank string, and the same story repeats for the next character i.e. i+1 

                The loop will do this over and over till it totally prints the word with maximum characters (thanks to ; for i in range(maxx))

                That's it



            
        '''

        s = s.split()
        maxx = max(len(x) for x in s) # Taking the max of length of words available in list s 
        for i in range(maxx): # Go over all till maxx length
            res = ""
            for x in s: # Jumping words at a time
                if i >=len(x):
                    res = res + ' '
                else:
                    res = res + str(x[i])
            final.append(res.rstrip()) # Why rstrip? If you jump words and the word is already over, It will append a whitespace to the right of the current letter, To remove that, rstrip() is used

        return final
        

            