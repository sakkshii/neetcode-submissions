class Solution:
    def isValid(self, s: str) -> bool:

        stack = deque()

        pairs = {
            "{" : "}",
            "[" : "]",
            "(" : ")"
        }
       
        for st in s:

            if st in pairs.keys():
                stack.append(st)
            else:
                if len(stack)==0:
                    return False
                top = stack.pop()
                val = pairs[top]
                if val == st:
                    continue
                else:
                    return False
                
        return True if len(stack)==0 else False
                





