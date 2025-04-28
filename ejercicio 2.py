def solve(expression: str) -> int:
    tokens = expression.split()
    stack = []
    i = 0
    while i < len(tokens):
        if tokens[i] == '*':

            prev = stack.pop()
            result = prev * int(tokens[i + 1])
            stack.append(result)
            i += 2
        elif tokens[i] == '+':

            i += 1
        else:
            stack.append(int(tokens[i]))
            i += 1
    return sum(stack)


print(solve("2 + 7 * 2 + 1"))
print(solve("2 * 2 * 2 + 32 * 2")) 
