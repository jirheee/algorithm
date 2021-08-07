from sys import stdin

if __name__ == "__main__":
    n = int(stdin.readline())
    equation = list(stdin.readline().strip())
    values = {chr(65+i):int(stdin.readline().strip()) for i in range(n)}
    stack = []

    for literal in equation:
        if literal in ['*', '+', '/', '-']:
            second = stack.pop()
            first = stack.pop()
            stack.append(eval(f"{first}{literal}{second}"))
        else:
            stack.append(values[literal])
    
    print(f"{stack[-1]:.2f}")