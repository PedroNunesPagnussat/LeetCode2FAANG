

class Solution: 

    class Stack():

        class Node():
            def __init__(self, value) -> None:
                self.value = value
                self.next = next
                
        def __init__(self):
            self.top = None
            self.length = 0

        def pop(self):
            top = self.top
            self.top = self.top.next
            self.length -= 1
            return top
        
        def push(self, value):
            node = self.Node(value)
            if self.length != 0:
                node.next = self.top
            self.top = node
            self.length += 1

            
    # Chad List Implementation
    def isValid(self, s: str) -> bool:
        stack = self.Stack()

        if len(s) % 2 == 1:
            return False
        
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for char in s:
            if char in pairs:
                stack.push(char)
            else:
                if stack.length == 0 or pairs[stack.pop().value] != char:
                    return False
        
        return stack.length == 0
        

    # Boring List Implementation
    def isValid(self, s: str) -> bool:
        stack = []

        if len(s) % 2 == 1:
            return False
        
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for char in s:
            if char in pairs:
                stack.append(char)
            else:
                if len(stack) == 0 or pairs[stack.pop()] != char:
                    return False
        
        return len(stack) == 0

        

if __name__ == '__main__':
    s = '(())'
    solution = Solution()
    answer = solution.isValid(s)
    print(answer)


