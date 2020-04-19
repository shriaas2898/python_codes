class Solution:
    def checkValidString(self, s: str) -> bool:
        
        stack = ['-']
        stars = ['-']
        for i in s:
            if i == ')':
                if '(' in stack:
                    stack[len(stack)- stack[::-1].index('(')] = '-'
                else:
                    stack.append(i)
                    stars.append('-')
                    #stars.append(i)
            elif i == '(':
                stack.append(i)
                stars.append('-')
            else:
                stars.append(i)
                stack.append('-')
                
        print(stack,stars)
        
        if ('(' in stack or ')' in stack):
            try:
                for i in range(len(stack)):
                    if stack[i] == '(' and i<stars.index('*'):
                        stars[stars.index('*')]=stack[i] = '-'
                    elif stack[i] == ')' and i>stars.index('*'):
                        stars[stars.index('*')]=stack[i] = '-'
                
            except ValueError:
                return False
            finally:
                del stack,stars
        else:
            if not ('(' in stack or ')' in stack):
                return True
