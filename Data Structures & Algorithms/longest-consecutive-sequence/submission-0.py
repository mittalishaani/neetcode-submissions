class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for num in numset:
            if (num - 1) not in numset:  # not the non first element of the consecutive sequence
                length = 1  # start
                while (
                    num + length
                ) in numset:  # num+length=(length)th element of the consecutive found sequence
                    length += 1
                longest = max(length, longest)  # update longest if length>longest
        return longest
