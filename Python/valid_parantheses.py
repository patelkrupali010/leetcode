
# #  use stack data type
# 
#  Each time, when an open parentheses is encountered push it in the stack
# 
# and when closed parenthesis is encountered, match it with the top of stack and pop it.
# 
#  If stack is empty at the end, return True otherwise, False.

def isValid(s):
    stack = []
    dict1 = { ')': '(', ']': '[', '}': '{' }
    #check if string is empty or not
    if s != '':
        for char in s:
            #  opening bracket
            if char in dict1:
                #check if stack is not empty and top element of stack is present in dictionary 
                if stack and stack[-1] == dict1[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
    else:
        return False
# return false if stack is not empty else true
    return False if stack else True

s = "{}"
isValid(s)
