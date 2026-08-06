class Solution:
    def isValid(self, s: str) -> bool:
        # If len 1 or starting with a closing bracket impossible so return true
        if(len(s)==1 or s[0] == ")" or s[0] == "}" or s[0] == "]"):
            return False
        stack = []
        dictionary = {"(":")", "[":"]", "{":"}"}
        metclose = False
        for ch in s:
            if(ch not in dictionary):
                metclose = True
                # Because append always insert an element to the largest index we need to recall by [-1]
                if(stack and ch == dictionary[stack[-1]]):
                    # Remove the end of the stack
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        if(metclose != True or  len(stack) >=1):
            return False
        return True