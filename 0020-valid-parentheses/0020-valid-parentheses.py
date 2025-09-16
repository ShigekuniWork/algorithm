class Solution:
    def isValid(self, s: str) -> bool:
        # I will use a stack to solve this problem.
        # We store open brackets in the stack.
        # Iterate through the string and check whether the current closing bracket
        # matches the corresponding opening bracket from the stack.
        # If we encounter an invalid match or the stack is not empty at the end, return False.
        # Otherwise, return True.
        
        # Initialize stack to store the opening brackets.
        stack = []
        # Initialize pairs ot the corresponding brackets.
        mapping = {')': '(', ']': '[', '}': '{'}
        
        # Iterate through the string.
        for c in s:
            # If the character is a closing bracket, check for a match.
            if c in mapping:
                if not stack or stack.pop() != mapping[c]:
                    return False
            else:
                # Otherwise, it must be an opening bracket, so push it to the stack.
                stack.append(c)
        
        # Check whether the stack is empty.
        return not stack
