import math
import sys
import copy
import collections
from itertools import combinations
from collections import deque

def init():
    N, Q = map(int, input().split())
    grid = []
    for _ in range(2**N):
        grid += list(map(int, input().split())),
    levels = list(map(int, input().split()))
    return N, Q, grid, levels


def rotate(grid, level, rows, cols):
    if 0 == level:
        return grid

    part_len = 2**level
    unit_len = 2**level//2
    #ngrid = copy.deepcopy(grid)
    ngrid = [[0]*cols for _ in range(rows)]

    # print(level)
    # print(part_len)
    # print(unit_len)

    # for sy in range(0, rows, part_len):
    #     for sx in range(0, cols, part_len):
    #         for dy, dx, oy, ox in [(0, 1, 0, 0), (1, 0, 0, unit_len), \
    #                 (-1, 0, unit_len, 0), (0, -1, unit_len, unit_len)]:

    #             cur_sy = sy + oy
    #             cur_sx = sx + ox

    #             for y in range(cur_sy, cur_sy + unit_len, 1):
    #                 for x in range(cur_sx, cur_sx + unit_len, 1):
    #                     ngrid[y + unit_len*dy][x + unit_len*dx] = \
    #                         grid[y][x]

    part_len = 2 ** level
    for y in range(0, rows, part_len):
        for x in range(0, cols, part_len):
            for i in range(part_len):
                for j in range(part_len):
                    ngrid[y + j][x + part_len - i - 1] = grid[y + i][x + j]


    return ngrid


def shrink_ice(grid, rows, cols):
    melt_coords = []

    for y in range(rows):
        for x in range(cols):
            cnt = 0

            for ny, nx in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
                if not (0 <= ny < rows and 0 <= nx < cols):
                    continue

                if 0 < grid[ny][nx]:
                    cnt += 1

            if cnt < 3 and grid[y][x]:
                melt_coords += (y, x),

    for y, x in melt_coords:
        grid[y][x] -= 1


def find_biggest_area(grid, rows, cols, part_len):
    visited = set()
    mx_cnt = 0

    for y in range(rows):
        for x in range(cols):
            if (y, x) in visited:
                continue

            if 0 == grid[y][x]:
                continue

            cnt = 1
            q = [(y, x)]
            visited.add((y, x))

            while q:
                cy, cx = q.pop(0)

                for ny, nx in [(cy + 1, cx), (cy - 1, cx), (cy, cx + 1), (cy, cx - 1)]:
                    if not (0 <= ny < rows and 0 <= nx < cols):
                        continue

                    if (ny, nx) in visited:
                        continue

                    if 0 == grid[ny][nx]:
                        continue

                    visited.add((ny, nx))
                    q += (ny, nx),
                    cnt += 1

            mx_cnt = max(mx_cnt, cnt)

    return mx_cnt


def sol():
    N, Q, grid, levels = init()
    rows, cols = len(grid), len(grid[0])

    for level in levels:
        grid = rotate(grid, level, rows, cols)
        shrink_ice(grid, rows, cols)

    #print_grid(grid)

    tot_ice = 0
    for line in grid:
        for val in line:
            tot_ice += val

    mx_cnt = find_biggest_area(grid, rows, cols, 2**N)

    print(tot_ice)
    print(mx_cnt)
    return tot_ice, mx_cnt

sol()