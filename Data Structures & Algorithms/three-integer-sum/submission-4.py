class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        #we fix one number and use 2 pointers for the other two

        for i in range(len(nums)): #fixing nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue #skip duplicates
            j = i + 1
            k = len(nums) - 1
            target = -nums[i]
            while j < k:
                
                if nums[j] + nums[k] < target:
                    j += 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]]) #we need all triplets so append instead of returning the triplet
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]: #skipping duplicate triplets(as in duplicate values in nums[j]) (the exact list item isnt being repeated, but atq triplets should be unique)
                        j += 1
        return res
