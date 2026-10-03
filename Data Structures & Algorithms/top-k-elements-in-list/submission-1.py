class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #initialize dictionary
        for num in nums:
            count[num] = 1 + count.get(num, 0) # for every number, get the previous count of that num (0 if it doesnt exist in the list yet), add 1 to it, then update it as the current count of that num
        arr = [] #we are creating an array of arrays here because we cant natively sort dicts
        for num, cnt in count.items(): # count.items() gives all key value pairs in the dictionary
            arr.append([cnt, num]) # add each pair to the array in this format
        arr.sort() # sort based on 1st item, which in this case is cnt

        result = []
        while len(result) < k:
            x = arr.pop()
            result.append(x[1])
        return result