from sys import stdin

def solve(input_string):
    count = 0
    ptr = 0
    while ptr<len(input_string):
        stack = [ptr]
        ptr += 1
        stick_count = 0
        group_count = 0
        while stack:
            if input_string[ptr] == "(":
                stack.append(ptr)
            else:
                popped = stack.pop()
                if ptr - popped == 1:
                    group_count += len(stack)
                else:
                    stick_count += 1
            ptr += 1
                
        count += group_count + stick_count
    return count



if __name__ == "__main__":
    input_string = stdin.readline().strip()

    print(solve(input_string))

