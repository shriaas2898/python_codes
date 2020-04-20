class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = ['-']
        for i in s:
            if i == ')':
                if '(' in stack:
                    stack.pop(len(stack)-1- stack[::-1].index('('))
                    continue
            stack.append(i)
        
        stack.append('-')
        print(stack)

        if '(' in stack or ')' in stack:
            stack2  = []
            idx = 0
            for i in stack[1:-1]:
                idx += 1
                print(stack,stack2,idx)
                if i == ')':
                    if '*' in stack2:
                        stack2.pop(len(stack2)-1- stack2[::-1].index('*'))
                        continue
                elif i == '(':
                    if '*' in stack[idx:] :
                        stack.pop(idx+stack[idx:].index('*'))
                        idx -= 1
                        continue
                stack2.append(i)
            stack = stack2
        print(stack)
        

        
        if (not('(' in stack or ')' in stack)):
            return True
        else:
            return False
            
       
