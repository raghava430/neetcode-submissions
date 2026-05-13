class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtrack(open_count, close_count):
            # Base case: used n open and n close parentheses
            if open_count == n and close_count == n:
                res.append("".join(stack))
                return

            # Add "(" if we still can
            if open_count < n:
                stack.append("(")
                backtrack(open_count + 1, close_count)
                stack.pop()

            # Add ")" only if it does not make string invalid
            if close_count < open_count:
                stack.append(")")
                backtrack(open_count, close_count + 1)
                stack.pop()

        backtrack(0, 0)
        return res