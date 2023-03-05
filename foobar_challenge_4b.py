'''
Running with Bunnies
====================

You and the bunny workers need to get out of this collapsing death trap of a
space station -- and fast! Unfortunately, some of the bunnies have been weakened
by their long work shifts and can't run very fast. Their friends are trying to
help them, but this escape would go a lot faster if you also pitched in. The
defensive bulkhead doors have begun to close, and if you don't make it through
in time, you'll be trapped! You need to grab as many bunnies as you can and get
through the bulkheads before they close.

The time it takes to move from your starting point to all of the bunnies and to
the bulkhead will be given to you in a square matrix of integers. Each row will
tell you the time it takes to get to the start, first bunny, second bunny, ...,
last bunny, and the bulkhead in that order. The order of the rows follows the
same pattern (start, each bunny, bulkhead). The bunnies can jump into your arms,
so picking them up is instantaneous, and arriving at the bulkhead at the same
time as it seals still allows for a successful, if dramatic, escape. (Don't
worry, any bunnies you don't pick up will be able to escape with you since they
no longer have to carry the ones you did pick up.) You can revisit different
spots if you wish, and moving to the bulkhead doesn't mean you have to
immediately leave -- you can move to and from the bulkhead to pick up additional
bunnies if time permits.

In addition to spending time traveling between bunnies, some paths interact with
the space station's security checkpoints and add time back to the clock. Adding
time to the clock will delay the closing of the bulkhead doors, and if the time
goes back up to 0 or a positive number after the doors have already closed, it
triggers the bulkhead to reopen. Therefore, it might be possible to walk in a
circle and keep gaining time: that is, each time a path is traversed, the same
amount of time is used or added.

Write a function of the form solution(times, time_limit) to calculate the most
bunnies you can pick up and which bunnies they are, while still escaping through
the bulkhead before the doors close for good. If there are multiple sets of
bunnies of the same size, return the set of bunnies with the lowest worker IDs
(as indexes) in sorted order. The bunnies are represented as a sorted list by
worker ID, with the first bunny being 0. There are at most 5 bunnies, and
time_limit is a non-negative integer that is at most 999.

For instance, in the case of
[
  [0, 2, 2, 2, -1],  # 0 = Start
  [9, 0, 2, 2, -1],  # 1 = Bunny 0
  [9, 3, 0, 2, -1],  # 2 = Bunny 1
  [9, 3, 2, 0, -1],  # 3 = Bunny 2
  [9, 3, 2, 2,  0],  # 4 = Bulkhead
]
and a time limit of 1, the five inner array rows designate the starting point,
bunny 0, bunny 1, bunny 2, and the bulkhead door exit respectively.
You could take the path:

Start End Delta Time Status
    -   0     -    1 Bulkhead initially open
    0   4    -1    2
    4   2     2    0
    2   4    -1    1
    4   3     2   -1 Bulkhead closes
    3   4    -1    0 Bulkhead reopens; you and the bunnies exit

With this solution, you would pick up bunnies 1 and 2. This is the best
combination for this space station hallway, so the solution is [1, 2].

Languages
=========

To provide a Java solution, edit Solution.java
To provide a Python solution, edit solution.py

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Java cases --
Input:
Solution({{0, 1, 1, 1, 1},
          {1, 0, 1, 1, 1},
          {1, 1, 0, 1, 1},
          {1, 1, 1, 0, 1},
          {1, 1, 1, 1, 0}}, 3)
Output:
    [0, 1]

Input:
Solution({{0, 2, 2, 2, -1},
          {9, 0, 2, 2, -1},
          {9, 3, 0, 2, -1},
          {9, 3, 2, 0, -1},
          {9, 3, 2, 2, 0}}, 1)
Output:
    [1, 2]

-- Python cases --
Input:
solution([[0, 2, 2, 2, -1],
          [9, 0, 2, 2, -1],
          [9, 3, 0, 2, -1],
          [9, 3, 2, 0, -1],
          [9, 3, 2, 2, 0]], 1)
Output:
    [1, 2]

Input:
solution([[0, 1, 1, 1, 1],
          [1, 0, 1, 1, 1],
          [1, 1, 0, 1, 1],
          [1, 1, 1, 0, 1],
          [1, 1, 1, 1, 0]], 3)
Output:
    [0, 1]

Use verify [file] to test your solution and see how it does. When you are
finished editing your code, use submit [file] to submit your answer. If your
solution passes the test cases, it will be removed from your home folder.
'''

def solution(times, time_limit):
    def find_best_bunnies(bunnies, time_left):
        # Base case: if there are no more bunnies to pick up, return an empty list
        if not bunnies:
            return []

        # Try picking up the first bunny and see how many more bunnies we can pick up
        bunny_time = times[bunnies[0]][-1]
        with_bunny = [bunnies[0]] + find_best_bunnies(bunnies[1:], time_left - bunny_time)

        # Try not picking up the first bunny and see how many more bunnies we can pick up
        without_bunny = find_best_bunnies(bunnies[1:], time_left)

        # Return the set of bunnies that allows us to pick up the most bunnies
        if len(with_bunny) > len(without_bunny):
            return with_bunny
        elif len(with_bunny) < len(without_bunny):
            return without_bunny
        else:
            # If both options allow us to pick up the same number of bunnies, return the set of bunnies with the lowest worker IDs
            return with_bunny if with_bunny[0] < without_bunny[0] else without_bunny

    # Initialize the list of bunnies with the worker IDs of all bunnies except the starting point
    bunnies = list(range(1, len(times) - 1))
    return find_best_bunnies(bunnies, time_limit)

# Second solution
import copy

def BellmanFord(times, time_limit):
    """
    Bellman-Ford algorithm using all vertices as source.
    We pass in the time_limit to check, when there is a negative cycle,
    if it it reachable from the start.
    """
    # Initialization
    n = len(times)
    d = [n*[float("inf")] for _ in range(n)]
    for s in range(n):
        d[s][s] = 0
        # Relaxation
        for i in range(n-1):
            updated = False
            for u in range(n):
                for v in range(n):
                    distReach = d[s][u] + times[u][v]
                    if d[s][v] > d[s][u] + times[u][v]:
                        updated = True
                        d[s][v] = distReach
            # An optimization. It doesn't change the worst case, but well ...
            if not updated:
                break
        # Negative cycle detection
        for u in range(n):
            for v in range(n):
                if d[s][v] > d[s][u] + times[u][v] and d[0][u] < time_limit:
                    return True, d # Negative cycle
    return False, d # no negative cycles


def solution(times, time_limit):
    n = len(times)
    if n <=2 :
        return []
    nc, d = BellmanFord(times, time_limit)
    if nc:
        return [x for x in range(len(times)-2)]
    else:
        # BFS for paths that collect max bunnies.
        stack = [[0,[0],time_limit,[[i] for i in range(n)]]]
        vertices = set([i for i in range(n)])
        maxBunnies = set()
        maxNumberBunnies = 0
        while stack:
            [u,path,timeleft, voidvertices] = stack.pop()
            for v in vertices - set(voidvertices[u]):
                timeuv = d[u][v]
                timeub = d[v][n-1]
                timevu = d[v][u]
                nextVoidVertices = copy.deepcopy(voidvertices)
                if timeuv+timevu == 0:
                    nextVoidVertices[u].append(v)
                    nextVoidVertices[v].append(u)
                if timeleft-timeuv-timeub >= 0:
                    nextPath = path+[v]
                    nextTimeLeft=timeleft-timeuv
                    stack.append([v,nextPath,nextTimeLeft,nextVoidVertices])
                    if v == n-1:
                        setNextPath = set(nextPath)
                        lengthNextPath = len(setNextPath)
                        if lengthNextPath == n: # We got all bunnies
                            return [x for x in range(len(times)-2)]
                        if maxNumberBunnies < lengthNextPath or (maxNumberBunnies == lengthNextPath and sum(maxBunnies) > sum(setNextPath)):
                            maxBunnies = setNextPath
                            maxNumberBunnies = lengthNextPath
        return sorted([x-1 for x in (maxBunnies - set([0,n-1]))])

# Third solution

def solution(times, times_limit):
    n = len(times)
    m = n-1
    dp = [[x for x in t] for t in times]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                dp[j][k] = min(dp[j][k], dp[j][i] + dp[i][k])

    for i in range(n):
        if dp[i][i] < 0:
            return [x-1 for x in range(1, m)]
    visited = [0] * n

    def dfs(x, limit):
        if limit < dp[x][m] or visited[x] > n:
            return []

        if x == m:
            if 0 not in visited:
                return [i for i in range(n)]
            do_dfs = False
            for i in range(1, m):
                if visited[i] == 0 and dp[x][i]+dp[i][x] <= limit:
                    do_dfs = True
            if not do_dfs:
                return [i for i in range(n) if visited[i] > 0 or i == m]

        res = []

        visited[x] += 1

        for i in range(n):
            if i == x:
                continue
            r = dfs(i, limit - times[x][i])
            if len(r) == n:
                res = r
                break
            if len(r) > len(res):
                res = r
            elif len(r) == len(res):
                for i in range(len(r)):
                    if r[i] < res[i]:
                        res = r
                        break
        visited[x] -= 1
        return res

    result = dfs(0, times_limit)
    result = [r-1 for r in result if r in range(1, m)]

    return result