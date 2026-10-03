class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [0] * n #all prefix products
        suff = [0] * n #all suffix products
        res = [0] * n #final result

        pref[0] = 1
        suff[n-1] = 1

        for i in range(1, n): #includes i=1, does not include i=n
            pref[i] = pref[i-1] * nums[i-1]
        for i in range(n-2, -1, -1): #range(start, stop, step)
            suff[i] = suff[i+1] * nums[i+1]
        for i in range(n): #loop through the numbers 0 to n-1.
            res[i] = pref[i] * suff[i]

        return res