class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def valid(s):
            count = 0

            for ch in s:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1

                    if count < 0:
                        return False

            return count == 0

        level = {s}

        while level:
            ans = [x for x in level if valid(x)]

            if ans:
                return ans

            next_level = set()

            for x in level:
                for i in range(len(x)):
                    if x[i] in '()':
                        next_level.add(x[:i] + x[i + 1:])

            level = next_level