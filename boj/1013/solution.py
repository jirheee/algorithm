import sys

def verify_signal(signal: str) -> bool:
    # (100+1+ | 01)+
    graph = {
        0: (1, 3),
        1: (None, 2),
        2: (1, 3),
        3: (4, None),
        4: (5, None),
        5: (5, 6),
        6: (1, 7),
        7: (8, 7),
        8: (5, 0),
    }

    state = 0
    for char in map(int, signal):
        # print(f"char: {char} state: {state} paths: {graph[state]}")
        state = graph[state][char]
        if state == None:
            return False
        
    return state in [0, 2, 6, 7]

if __name__ == "__main__":
    n = int(sys.stdin.readline())

    signals = [sys.stdin.readline().strip() for  _ in range(n)]

    for signal in signals:
        if verify_signal(signal):
            print("YES")
        else:
            print("NO")