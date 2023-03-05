# -*- coding: utf-8 -*-

'''
Prepare the Bunnies' Escape
===========================

You're awfully close to destroying the LAMBCHOP doomsday device and freeing
Commander Lambda's bunny workers, but once they're free of the work duties the
bunnies are going to need to escape Lambda's space station via the escape pods
as quickly as possible. Unfortunately, the halls of the space station are a maze
of corridors and dead ends that will be a deathtrap for the escaping bunnies.
Fortunately, Commander Lambda has put you in charge of a remodeling project
that will give you the opportunity to make things a little easier for the
bunnies. Unfortunately (again), you can't just remove all obstacles between the
bunnies and the escape pods - at most you can remove one wall per escape pod
path, both to maintain structural integrity of the station and to avoid arousing
Commander Lambda's suspicions. 

You have maps of parts of the space station, each starting at a work area exit
and ending at the door to an escape pod. The map is represented as a matrix of
0s and 1s, where 0s are passable space and 1s are impassable walls. The door out
of the station is at the top left (0,0) and the door into an escape pod is at
the bottom right (w-1,h-1). 

Write a function solution(map) that generates the length of the shortest path
from the station door to the escape pod, where you are allowed to remove one
wall as part of your remodeling plans. The path length is the total number of
nodes you pass through, counting both the entrance and exit nodes. The starting
and ending positions are always passable (0). The map will always be solvable,
though you may or may not need to remove a wall. The height and width of the map
can be from 2 to 20. Moves can only be made in cardinal directions; no diagonal
moves are allowed.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit Solution.java

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution([[0, 1, 1, 0],
                   [0, 0, 0, 1],
                   [1, 1, 0, 0],
                   [1, 1, 1, 0]])
Output:
    7

Input:
solution.solution([[0, 0, 0, 0, 0, 0],
                   [1, 1, 1, 1, 1, 0],
                   [0, 0, 0, 0, 0, 0],
                   [0, 1, 1, 1, 1, 1],
                   [0, 1, 1, 1, 1, 1],
                   [0, 0, 0, 0, 0, 0]])
Output:
    11

-- Java cases --
Input:
Solution.solution({{0, 1, 1, 0},
                   {0, 0, 0, 1}, 
                   {1, 1, 0, 0}, 
                   {1, 1, 1, 0}})
Output:
    7

Input:
Solution.solution({{0, 0, 0, 0, 0, 0}, 
                   {1, 1, 1, 1, 1, 0}, 
                   {0, 0, 0, 0, 0, 0}, 
                   {0, 1, 1, 1, 1, 1}, 
                   {0, 1, 1, 1, 1, 1}, 
                   {0, 0, 0, 0, 0, 0}})
Output:
    11
'''

def solution2(map):
    # A* using Manhattan distance with 1 optional removal of a wall
    door = (len(map) - 1, len(map[0]) - 1)
    visited = set()
    queue = [[True, 1, (0, 0)]]
    # While queue, if neighbor node is door, return steps + 1, if node (under removal state) already visited, continue
    # If not, mark as visited, add all possible moves to queue and sort queue by steps + Manhattan distance
    while queue:
        e = queue.pop(0)
        removal, steps, node = e[0], e[1], e[2]
        if (removal, node) in visited:
            continue
        visited.add((removal, node))
        for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ny, nx = node[0] + dy, node[1] + dx
            if 0 <= ny <= door[0] and 0 <= nx <= door[1]:
                if (ny, nx) == door:
                    return steps + 1
                elif map[ny][nx] == 0:
                    queue += [[removal, steps + 1, (ny, nx)]]
                elif removal:
                    queue += [[False, steps + 1, (ny, nx)]]
        queue = sorted(queue, key=lambda x: x[1] + door[0] - x[2][0] + door[1] - x[2][1] + 1)

from collections import deque

def solution(map):
    m, n = len(map), len(map[0])
    move_directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    def breadth_first_search(i, j):
        matrix = [[None] * n for _ in range(m)]
        matrix[i][j] = 1
        
        queue = deque([(i, j)])
        while queue:
            x, y = queue.popleft()
            for move_x, move_y in move_directions:
                new_x, new_y = x + move_x, y + move_y
                if 0 <= new_x < m and 0 <= new_y < n:
                    if matrix[new_x][new_y] is None:
                        matrix[new_x][new_y] = matrix[x][y] + 1
                        if map[new_x][new_y] == 1: continue
                        queue.append((new_x, new_y))
        return matrix
    start = breadth_first_search(0, 0)
    end = breadth_first_search(m - 1, n - 1)
    result = float('inf')
    for i in range(m):
        for j in range(n):
            if start[i][j] and end[i][j]:
                result = min(result, start[i][j] + end[i][j] - 1)
    return result


print(solution([[0, 1, 1, 0],
                [0, 0, 0, 1],
                [1, 1, 0, 0],
                [1, 1, 1, 0]]))

print(solution([[0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1],
                [0, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0]]))

print(solution([[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]))

# path 1 is 57 long, one wall removed gives 45
# path 2 is 70 long, one wall removed gives 39