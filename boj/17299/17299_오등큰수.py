from sys import stdin

def solve(seq):
    
    count_list = {}
    for num in seq:
        if num in count_list:
            count_list[num] +=1
        else:
            count_list[num] = 1
    
    result = [-1 for _ in seq]
    stack = [0]

    for i in range(1, len(seq)):
        while stack and count_list[seq[stack[-1]]] < count_list[seq[i]]:
            result[stack.pop()] = seq[i]
        
        stack.append(i)
    
    return " ".join(map(str,result))


if __name__ == "__main__":
    n = int(stdin.readline())
    seq = list(map(int, stdin.readline().strip().split()))

    print(solve(seq))