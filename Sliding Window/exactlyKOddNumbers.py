class Solution:

    # Logic: Sliding window brilliancy ; With hashmap
    # def numberOfSubarrays(self, nums: List[int], k: int) -> int:

    #     l , windowcount = 0 , 0
    #     count = 0
    #     ans = 0

    #     hashmap = {}

    #     for i in range(len(nums)):
    #         if nums[i] % 2 == 1:
    #             hashmap[nums[i]] = hashmap.get(nums[i] , 0) + 1
    #             count+=1
    #             windowcount = 0
            
    #         while count == k:
    #             windowcount+=1

    #             if nums[l] % 2 == 1:
    #                 hashmap[nums[l]]-=1
    #                 count-=1
    #                 if hashmap[nums[l]] == 0:
    #                     hashmap.pop(nums[l])
    #             l+=1
    #         ans+=windowcount
            
    #     return ans

    # Logic: What if I told you that you can ditch the hashmap?

    '''
        So many questions, Let's take them one at a time.

        Why 3 variables? ans , count and windowcount?

        That's pretty neat actually, You know why?
        The count holds the count of odds accounted for, i.e The odds currently in the subarray.
        So good! Why cant I directly return windowcount then? Hold your horses.

        We need to account for each and every window, That means we cannot slide past that one odd number which will turn our subarray invalid, or can we?

        That's where windowcount being separate comes into picture.
        I'll mantain a windowcount and everytime I'll encounter a new odd element I'll reset it to 0
        Perfect. The real pictures comes in when count == k

        Let's go inside the while loop:
        When count == k, We incrememnt the windowcount definitely, But we also have to slide the left ptr, How do we do that?

        Well do NOT decrement count when the element you're removing is not odd, That makes perfect sense, Okay. Now the moment comes, You're throwing out the last odd element which made your array valid, Good, Throw it out, We dont need it anymore, The result is already kept in WINDOWCOUNT

        As long as i keeps increasing, ans will be incremented with windoecount, So even if we don't encounter any count == k cases, i.e. no more odd elements, Our answer will be precise

        And what if we encounter, windowcount = 0 will occur and will be again set in the same way

        That's it

        The last question,
        Why would you need hashmap in this?
        Are you keeping a frequency of something, Are you using len(hashmap) somewhere, Is it unique k characters or atleast k unique or atleast k different kind of frequency bullshit? No right?
        So you can ditch the hashmap

        And kid, Congratulations on building up the top submissions sliding window solution all by yourself, Not to shabby, Keep working hard

        That's it, Cool, Easy
    '''


    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l , windowcount = 0 , 0
        count = 0
        ans = 0

        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                count+=1
                windowcount = 0
            
            while count == k:
                windowcount+=1

                if nums[l] % 2 == 1:
                    count-=1
                l+=1
            ans+=windowcount
            
        return ans