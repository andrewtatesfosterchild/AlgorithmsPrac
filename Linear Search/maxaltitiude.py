class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        # Logic: Linear searching bs prob
        '''
            No need to make an array and complicate things
            For each gain, sum it up and add it to alt, If > maxalt, maxalt = alt
            If result -ve, return 0 else maxalt
            That's it :/
        '''
        maxalt = -1
        alt = 0

        for i in range(len(gain)):
            alt = alt + gain[i]
            if alt > maxalt:
                maxalt = alt

        return maxalt if maxalt>0 else 0
