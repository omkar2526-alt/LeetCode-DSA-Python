class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        freq = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for i in range(len(s)):

            if s[i] in "([{":
                stack.append(s[i])

            elif s[i] in freq:

                if not stack:
                    return False

                if freq[s[i]] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0


# Testing
solution = Solution()

tests = [
    "()",
    "()[]{}",
    "(]",
    "([{}])",
    "(((",
    "]"
]

for test in tests:
    print(test, "→", solution.isValid(test))