from sys import stdin
import math

def get_max_cd(num_digits: int, max_digits: int) -> int:
    if num_digits == 1:
        return 0
    return (max_digits - 1) // (num_digits - 1)

def is_square_number(number: str) -> bool:
    sqrt = math.sqrt(int(number))
    return sqrt == int(sqrt)

def get_square_nums(table: list[str], row_cd: int, col_cd: int, num_digits: int, n: int, m: int) -> list[str]:

    max_row_offset = n if row_cd == 0 else n - num_digits * row_cd + 1
    row_idx_sets = [[i*row_cd + offset for i in range(num_digits)] for offset in range(max(max_row_offset, 1))]
    row_idx_sets += [ris[::-1] for ris in row_idx_sets]

    max_col_offset = m if col_cd == 0 else m - num_digits * col_cd + 1
    col_idx_sets = [[i*col_cd + offset for i in range(num_digits)] for offset in range(max(max_col_offset, 1))]
    col_idx_sets += [cis[::-1] for cis in col_idx_sets]

    def get_num_by_idx_sets(row_idx_set, col_idx_set):
        num = "".join(map(lambda x: table[x[0]][x[1]] ,zip(row_idx_set, col_idx_set)))
        return num

    nums = [get_num_by_idx_sets(row_idx_set, col_idx_set) for row_idx_set in row_idx_sets for col_idx_set in col_idx_sets]

    return filter(is_square_number, nums)

def solve(n: int, m: int, table: list[str]) -> int:
    max_digits = max(n, m)

    for num_digits in range(max_digits, 0, -1):
        max_row_cd = get_max_cd(num_digits, n)
        max_col_cd = get_max_cd(num_digits, m)

        square_numbers = []

        for row_cd in range(max_row_cd + 1):
            for col_cd in range(max_col_cd + 1):
                square_numbers += get_square_nums(table, row_cd, col_cd, num_digits, n, m)

        if num_digits > 1:
            square_numbers = list(filter(lambda x: x[0] != "0", square_numbers))
            if square_numbers:
                return max(map(int, square_numbers))
        elif square_numbers:
            return max(map(int, square_numbers))
    
    return -1

if __name__ == "__main__":
    n, m = [int(i) for i in stdin.readline().split()]

    table = [stdin.readline().strip() for _ in range(n)]

    print(solve(n, m, table))