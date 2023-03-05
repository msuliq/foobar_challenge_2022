# -*- coding: utf-8 -*-
'''
Bomb, Baby!
===========

You're so close to destroying the LAMBCHOP doomsday device you can taste it! But
in order to do so, you need to deploy special self-replicating bombs designed
for you by the brightest scientists on Bunny Planet. There are two types: Mach
bombs (M) and Facula bombs (F). The bombs, once released into the LAMBCHOP's
inner workings, will automatically deploy to all the strategic points you've
identified and destroy them at the same time. 

But there's a few catches. First, the bombs self-replicate via one of two
distinct processes: 
Every Mach bomb retrieves a sync unit from a Facula bomb; for every Mach bomb, a
Facula bomb is created;
Every Facula bomb spontaneously creates a Mach bomb.

For example, if you had 3 Mach bombs and 2 Facula bombs, they could either
produce 3 Mach bombs and 5 Facula bombs, or 5 Mach bombs and 2 Facula bombs. The
replication process can be changed each cycle. 

Second, you need to ensure that you have exactly the right number of Mach and
Facula bombs to destroy the LAMBCHOP device. Too few, and the device might
survive. Too many, and you might overload the mass capacitors and create a
singularity at the heart of the space station - not good! 

And finally, you were only able to smuggle one of each type of bomb - one Mach,
one Facula - aboard the ship when you arrived, so that's all you have to start
with. (Thus it may be impossible to deploy the bombs to destroy the LAMBCHOP,
but that's not going to stop you from trying!) 

You need to know how many replication cycles (generations) it will take to
generate the correct amount of bombs to destroy the LAMBCHOP. Write a function
solution(M, F) where M and F are the number of Mach and Facula bombs needed.
Return the fewest number of generations (as a string) that need to pass before
you'll have the exact number of bombs necessary to destroy the LAMBCHOP, or the
string "impossible" if this can't be done! M and F will be string
representations of positive integers no larger than 10^50. For example, if
M = "2" and F = "1", one generation would need to pass, so the solution would
be "1". However, if M = "2" and F = "4", it would not be possible.

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
Solution.solution('2', '1')
Output:
    1

Input:
Solution.solution('4', '7')
Output:
    4

-- Python cases --
Input:
solution.solution('4', '7')
Output:
    4

Input:
solution.solution('2', '1')
Output:
    1
'''

def solution(M, F):
    result = (int(M), int(F))
    start = (1, 1)
    iteration = [start]
    count = 0
    while iteration:
        # set up next iteration
        next_iteration = []
        for M,F in iteration:
            if (M,F) == result:
                return str(count)
            # add successful replications into next iteration
            MF = M+F
            if MF <= result[0]:
                next_iteration.append((MF, F))
            if MF <= result[1]:
                next_iteration.append((M, MF))
        # move to next iteration
        iteration = next_iteration
        count += 1
    return 'impossible'


def solution2(x, y):
    goal = (int(x), int(y))
    start = (1, 1)
    gen = set([start])
    c = 0
    while gen:

        if goal in gen:
            return str(c)
            
        # Generate new states
        next_gen = set()
        for M,F in gen:
            # Ignore states that never lead to goal
            MF = M+F
            if MF <= goal[0]:
                state = (MF, F)
                if state not in seen:
                    next_gen.add(state)
                    seen.add(state)
            if MF <= goal[1]:
                state = (M, MF)
                if state not in seen:
                    next_gen.add(state)
                    seen.add(state)
        
        # Go to next generation
        gen = next_gen
        c += 1

    return 'impossible'

# Let's assume that x is one type of bombs and y is the other and x may not
# equal to y to continue the replication cycle. So to calculate the shortest
# path to the needed amount of x and y:
# 1. We need to take path of x if there more of x, or y if there is more of y
# type bombs so we achieve best possible replication effectiveness.
# 2. Each replication cycle we need to add newly created bombs. If first we take
# path of x, then y type bombs will be created, and then at some point y will 
# become more in quantity that x to we will switch the variables around and take
# path of y.
# 3. Newly created bombs are calculated as: (whichever is more minus the less)
# floor divided by the less type, plus (whichever is more minus the less)
# modulus divided by the less type (if it's not less that 1), so we get the
# amount of newly as whole integer. 
# created less types of bombs.

def solution3(M, F):
    result = (int(M), int(F))
    mach, facula = result
    cycle_count = 0

    while mach!=facula:
        10 > 3
        (10-4)//4 + (10-4) % 4 > 0
        if mach > facula:
            num_subs = (mach-facula)//facula + ((mach-facula) % facula > 0)
            cycle_count += num_subs
            mach, facula = mach - num_subs * facula, facula
        elif facula > mach:
            num_subs = (facula-mach)//mach + ((facula-mach) % mach > 0)
            cycle_count += num_subs
            mach, facula = mach, facula - num_subs * mach
        
    return str(cycle_count) if (mach, facula)==(1, 1) else 'impossible'

print(solution3('4', '7'))
print(solution3('2', '1'))
print(solution3('2', '2'))
print(solution3('14', '14'))
print(solution3(str(10^50), str(9^50)))


