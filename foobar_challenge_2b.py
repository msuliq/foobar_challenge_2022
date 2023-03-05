'''
Hey, I Already Did That!
========================

Commander Lambda uses an automated algorithm to assign minions randomly to
tasks, in order to keep minions on their toes. But you've noticed a flaw in the
algorithm -- it eventually loops back on itself, so that instead of assigning
new minions as it iterates, it gets stuck in a cycle of values so that the same
minions end up doing the same tasks over and over again. You think proving this
to Commander Lambda will help you make a case for your next promotion. 

You have worked out that the algorithm has the following process: 

1) Start with a random minion ID n, which is a nonnegative integer of length k
in base b
2) Define x and y as integers of length k.  x has the digits of n in descending
order, and y has the digits of n in ascending order
3) Define z = x - y.  Add leading zeros to z to maintain length k if necessary
4) Assign n = z to get the next minion ID, and go back to step 2

For example, given minion ID n = 1211, k = 4, b = 10, then x = 2111, y = 1112
and z = 2111 - 1112 = 0999. Then the next minion ID will be n = 0999 and the
algorithm iterates again: x = 9990, y = 0999 and z = 9990 - 0999 = 8991, and so
on.

Depending on the values of n, k (derived from n), and b, at some point the
algorithm reaches a cycle, such as by reaching a constant value. For example,
starting with n = 210022, k = 6, b = 3, the algorithm will reach the cycle of
values [210111, 122221, 102212] and it will stay in this cycle no matter how
many times it continues iterating. Starting with n = 1211, the routine will
reach the integer 6174, and since 7641 - 1467 is 6174, it will stay as that
value no matter how many times it iterates.

Given a minion ID as a string n representing a nonnegative integer of length k
in base b, where 2 <= k <= 9 and 2 <= b <= 10, write a function solution(n, b)
which returns the length of the ending cycle of the algorithm above starting
with n. For instance, in the example above, solution(210022, 3) would return 3,
since iterating on 102212 would return to 210111 when done in base 3. If the
algorithm reaches a constant, such as 0, then the length is 1.

Languages
=========

To provide a Java solution, edit Solution.java
To provide a Python solution, edit solution.py

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Java cases --
Input:
Solution.solution('210022', 3)
Output:
    3

Input:
Solution.solution('1211', 10)
Output:
    1

-- Python cases --
Input:
solution.solution('1211', 10)
Output:
    1

Input:
solution.solution('210022', 3)
Output:
    3
'''


def solution(n, b):
    k = len(str(n))
    if (k >= 2 and k <= 9):
        def to_base_10(num,base):
            if base==10:
                return num
            else:
                num = str(num)
                leng = [x for x in num]
                i = 0
                j = 0
                for l in leng:
                    i += int(l)*base**((len(leng)-1)-j)
                    j+=1
                return i
                      
        def to_base_n(num,base):
            res = []
            if base==10:
                return num
            else:
                while num > 0:
                    i = num%base
                    res.append(str(i))
                    num = int(num/base)
                    res = res[::-1]
                    sol = "".join(res)
                    sol = int(sol)
            return sol
                    
        result = []
        while True:
            sol = str(n)
            x = list(sol)
            y = list(sol)
            x.sort(reverse=True)
            y.sort()
            x = int("".join(x))
            y = int("".join(y))
            x = to_base_10(x,b)
            y = to_base_10(y,b)
            z = x-y
            n = to_base_n(z,b)
            quick = str(n)
            list_n = [x for x in quick]
            while len(list_n) != k:
                list_n.insert(0,'0')
                n = "".join(list_n)
            if n not in result:
                result.append(n)
            else:
                return len(result) - result.index(n)
                
print(solution('1211', 10))
print(solution('210022', 3))
