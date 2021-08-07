from sys import stdin

def solve(string: str):
    l = []

    length = len(string)
    ptr = 0
    while ptr < length:
        end = ptr
        if string[ptr] == "<":
            while string[end] != ">":
                end+=1
            l.append(string[ptr:end+1])
            ptr = end + 1
        else:
            while end<length and string[end] != "<":
                end +=1
            split = [word[::-1] for word in string[ptr:end].split()]
            l.append(" ".join(split))
            ptr  = end
    
    return "".join(l)


if __name__ == "__main__":
    string = stdin.readline().strip()
    print(solve(string))