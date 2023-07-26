class Solution:
    # Logic: Binary search; Just like Koko eating bananas, Speed dangle search

    '''
        Binary search on steroids (Speed Dangle search like koko)

        The lowest speed is 1 and the highest speed is 10 ** 7 + 1 as it says the answer will not exceed 10 ** 7 + 1, That's the only difference.
        And lowest speed is 1 because well if it is 0 you won't f@cking move

        The only difference between this and koko is the rounding off part, The last value is not to be rounded off since we have reached the destination by then

        That's it
    '''
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        s = 1
        e = 10**7 + 1
        answer = -1

        while s < e:
            mid = s + (e-s) // 2

            totalhours = 0.0

            for i in range(len(dist) - 1): #why n-1? Because besides the last distance which we will calculate later, Everything needs to be rounded off, That's the reason last one is calculated outside the loop

                totalhours += (dist[i] + mid - 1) // mid # What is the significance of adding mid - 1 to numerator? The significance is that, It is a common technique used in rounding off and ensuring the answer is not truncated

            totalhours += dist[-1] / mid # Calculating the last one separately as it doesn't need rounding off, Because we have already reached the destination, So no need of rounding off

            if totalhours > hour:
                s = mid + 1
            else:
                e = mid

        return s if s!=10**7 + 1 else -1
