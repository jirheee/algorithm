import sys

def solve():
    stack = []
    string = sys.stdin.readline().strip()
    for i in range(len(string)):
        if string[i] == "(":
            stack.append("(")
        elif string[i] == ")" and len(stack) > 0 and stack.pop() == "(":
            continue
        else:
            return False
    
    return True if len(stack) == 0 else False
        
        
    

if __name__ =="__main__":
    n = int(sys.stdin.readline())
    for i in range(n):
        success = solve()
        print("YES" if success else "NO")
