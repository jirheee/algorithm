from sys import stdin
from typing import List

def solve(costs: List[List[int]], n):
    # redlowsetcost[i] = min(greenlowestcost[i-1], bluelowestcost[i-1]) + costs[i][0]
    red_lowest_cost = [0 for _ in range(n)]
    green_lowest_cost = [0 for _ in range(n)]
    blue_lowest_cost = [0 for _ in range(n)]

    red_lowest_cost[0] = costs[0][0]
    green_lowest_cost[0] = costs[0][1]
    blue_lowest_cost[0] = costs[0][2]

    for i in range(1, n):
        red_lowest_cost[i] = min(green_lowest_cost[i-1], blue_lowest_cost[i-1]) + costs[i][0]
        green_lowest_cost[i] = min(red_lowest_cost[i-1], blue_lowest_cost[i-1]) + costs[i][1]
        blue_lowest_cost[i] = min(green_lowest_cost[i-1], red_lowest_cost[i-1]) + costs[i][2]

    return min(red_lowest_cost[n-1], green_lowest_cost[n-1], blue_lowest_cost[n-1])

if __name__ == "__main__":
    n = int(stdin.readline())

    costs = [list(map(int, stdin.readline().strip().split())) for _ in range(n)]

    print(solve(costs, n))