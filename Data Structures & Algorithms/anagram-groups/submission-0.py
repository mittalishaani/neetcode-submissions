class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) #creates a dictionary with list values. will automatically initialize new keys with empty lists before appending
        for s in strs:
            count = [0] *26 #list of 26 zeroes
            for c in s: #for each character in string
                count[ord(c) -ord('a')] +=1 #inc frequency of that character, ord(c) returns unicode number of c
            result[tuple(count)].append(s) #makes a tuple of count as the key and appends s as the value
        return list(result.values()) #makes a new list of lists from values of the dict 