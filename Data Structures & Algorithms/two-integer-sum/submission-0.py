class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap={} #initialize an empty dict
        for i, n in enumerate(nums): #enumerate(nums) gives (index, value) one by one
            diff=target - n #calculate complement for current element
            if diff in prevMap: # if the complement already found in prevMap, solution has been found
                return [prevMap[diff], i] #[Map[complement val]->index, index of current value]
            prevMap[n]=i #else add current val to dict at its index as 
            #val->index