class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        # Logic: minHeap

        '''
            Basic idea of this problem is to find the k smallest pairs

            Boom sherlock, Now what -_-

            Arrays are sorted, Thus first two elements for the smallest pair
            Next, This means only 3 possibilites:
                1. pair formed by i + 1 , j is smallest
                2. pair formed by i , j + 1 is smallest

            Why not add them both in minheap and let minheap figure it out? 
            * Why heap?
            Because, A heap is a useful data structure when it is necessary to repeatedly remove the object with the lowest (or highest) priority, or when insertions need to be interspersed with removals of the objects.

            visited set stores the indices already visited

            The only notable steps in this problem are,

            minheap = [((nums1[0] + nums2[0]), (0,0))] # First two elements are always the smallest, and (0,0) is the index tuple

            val , (i,j) = heappop(minheap) # Removes the smallest element from minheap an assigns the sum to val and indices to i and j
            ans.append([nums1[i],nums2[j]])

            if i + 1 < m and (i + 1 , j) not in visited: # A check to append if list is not over and indices are not visited
                heappush(minheap , (nums1[i + 1] + nums2[j] , (i + 1 , j)))
                visited.add((i+1 , j))
            
            if j + 1 < n and (i , j + 1) not in visited: # same logic as above
                heappush(minheap , (nums1[i] + nums2[j+1], (i , j + 1)))
                visited.add((i , j + 1))

        In summary , the minheap is comparing between the leftover pair, The i + 1 , j pair and the i , j + 1 pair everytime and appending the smallest result

        That's it, :coinflipper: ;)



        '''

        m , n = len(nums1) , len(nums2) # 

        ans = []

        visited = set() # set to keep track of all things already visited

        minheap = [((nums1[0] + nums2[0]), (0,0))] # initializing minheap
        visited.add((0,0)) # First two elements always the smallest

        while k > 0 and minheap: # sets the break bounds when minheap is empty or enough pairs are returned
            val , (i,j) = heappop(minheap)
            ans.append([nums1[i],nums2[j]])

            if i + 1 < m and (i + 1 , j) not in visited: 
                heappush(minheap , (nums1[i + 1] + nums2[j] , (i + 1 , j)))
                visited.add((i+1 , j)) # Adding i + 1 , j to compare & remove in the upcoming
            
            if j + 1 < n and (i , j + 1) not in visited:
                heappush(minheap , (nums1[i] + nums2[j+1], (i , j + 1)))
                visited.add((i , j + 1)) # Adding i , j + 1 to compare & remove in the next iteration
            
            k-=1
        
        return ans