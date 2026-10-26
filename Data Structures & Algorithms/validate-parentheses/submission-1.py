class Solution:
    def isValid(self, s: str) -> bool:
        while '()' in s or '{}' in s or '[]' in s:
            s=s.replace('()', '')
            s=s.replace('{}', '')
            s=s.replace('[]', '')
        return s==''

# this works even in nested parentheses as the innermost parentheses valid pair is removed in every iteration. for {[()]} first () is removed and {[]} is left, then [] then {}