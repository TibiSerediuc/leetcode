class Solution:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        toks = {"+", "-", "/", "*"}

        for token in tokens:

            if token in toks:
                #the order we read the pops matter for division and subtraction
                elem1, elem2 = stack.pop(), stack.pop()
                if token == "+":
                    stack.append(elem1 + elem2)
                elif token == "-":
                    stack.append(elem2 - elem1)
                elif token == "/" and elem1 != 0:
                    stack.append(int(elem2 / elem1))
                elif token == "*":
                    stack.append(elem1 * elem2)
            else:
                stack.append(int(token))

        return stack.pop()