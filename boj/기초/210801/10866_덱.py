from sys import stdin

if __name__ == "__main__":
    n = int(stdin.readline())

    deque = []

    for _ in range(n):
        instr = stdin.readline().strip().split()

        if instr[0] == "push_front":
            deque.insert(0, instr[1])
        if instr[0] == "push_back":
            deque.append(instr[1])
        if instr[0] == "pop_front":
            print(deque.pop(0) if deque else -1)
        if instr[0] == "pop_back":
            print(deque.pop() if deque else -1)
        if instr[0] == "size":
            print(len(deque))
        if instr[0] == "empty":
            print(0 if deque else 1)
        if instr[0] == "front":
            print(deque[0] if deque else -1)
        if instr[0] == "back":
            print(deque[-1] if deque else -1)