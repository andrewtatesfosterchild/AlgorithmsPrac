class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

        # Logic: Array reversal + bit manipulation

        '''
            Simple and interesting 2D arr manipulation

            Reverse each row, flip the bits and do it all IN PLACE

            That's it, :coinflipper: ;)

        '''

        def reverse(row):
            
            i , j = 0 , len(row) - 1

            while i<j:
                temp = row[i]
                row[i] = row[j]
                row[j] = temp

                i+=1
                j-=1
            
            return row

        def bitflip(row):
            
            for i in range(len(row)):
                row[i] = 0 if row[i] == 1 else 1


        for row in image:
            row = bitflip(reverse(row))
        
        return image