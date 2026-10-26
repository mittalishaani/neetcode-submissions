class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] #declare list
        closetoopen = {')':'(', '}':'{', ']':'['}
        for c in s: #for every character in the string 
            if c in closetoopen: #if the character is a closing parentheses
                if stack and stack[-1]==closetoopen[c]: #if the stack is non empty and has the corresponding opening parentheses on top
                    stack.pop()
                else:

                    return False
            else: #if the character is an opening parentheses
                stack.append(c)
        return True if not stack else False