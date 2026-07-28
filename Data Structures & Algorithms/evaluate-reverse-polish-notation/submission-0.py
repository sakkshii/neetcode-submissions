class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = deque()
        
        for ch in tokens:
            if ch[-1].isdigit():
                stack.append(int(ch))
            else:
                top1 = stack.pop()
                top2 = stack.pop()

                if(ch == "+"):
                    stack.append(top2 + top1 )
                elif(ch == "-"):
                    stack.append(top2-top1)
                elif (ch == "*"):
                    stack.append(top2 * top1)
                elif (ch == "/"):
                    stack.append(int(top2/top1))
        return stack[0]





        