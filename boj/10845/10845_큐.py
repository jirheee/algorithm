from sys import stdin

if __name__ == "__main__":
    n = int(stdin.readline())

    queue = []

    for _ in range(n):
        instruction = stdin.readline().strip().split()

        if instruction[0] == "push":
            queue.append(int(instruction[1]))
        if instruction[0] == "pop":
            print(queue.pop(0) if len(queue)>0 else -1)
        if instruction[0] == "size":
            print(len(queue))
        if instruction[0] == "empty":
            print(1 if len(queue) == 0 else 0)
        if instruction[0] == "front":
            print(queue[0] if len(queue)>0 else -1)
        if instruction[0] == "back":
            print(queue[-1] if len(queue)>0 else -1)