class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append('#')
            res.append(s)
        return "".join(res) #joins all list items into a single string without any gap in between (the 2 consecutive "" do this)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s): # 1 iteration = 1 word
            j = i
            while s[j] != '#':
                j = j+1 #to find the delimiter
            length = int(s[i:j])
            j +=1
            i = j + length
            
            res.append(s[j:i])
            j = i
        return res
