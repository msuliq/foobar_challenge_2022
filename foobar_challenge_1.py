# -*- coding: utf-8 -*-
"""
Minion Work Assignments
=======================
Commander Lambda's minions are upset! They're given the worst jobs on the
whole space station, and some of them are starting to complain that even those
worst jobs are being allocated unfairly. If you can fix this problem, it'll
prove your chops to Commander Lambda so you can get promoted!

Minions' tasks are assigned by putting their ID numbers into a list, one time
for each day they'll work that task. As shifts are planned well in advance,
the lists for each task will contain up to 99 integers. When a minion is
scheduled for the same task too many times, they'll complain about it until
they're taken off the task completely. Some tasks are worse than others, so
the number of scheduled assignments before a minion will refuse to do a task
varies depending on the task.  You figure you can speed things up by
automating the removal of the minions who have been assigned a task too many
times before they even get a chance to start complaining.

Write a function called solution(data, n) that takes in a list of less than
100 integers and a number n, and returns that same list but with all of the
numbers that occur more than n times removed entirely. The returned list
should retain the same ordering as the original list - you don't want to mix
up those carefully-planned shift rotations! For instance, if data was [5, 10,
15, 10, 7] and n was 1, solution(data, n) would return the list [5, 15, 7]
because 10 occurs twice, and thus was removed from the list entirely.

Languages
=========
To provide a Python solution, edit solution.py
To provide a Java solution, edit Solution.java

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution([1, 2, 3], 0)
Output:
    

Input:
solution.solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 1)
Output:
    1,4

-- Java cases --
Input:
Solution.solution({1, 2, 3}, 0)
Output:
    

Input:
Solution.solution({1, 2, 2, 3, 3, 3, 4, 5, 5}, 1)
Output:
    1,4

Use verify [file] to test your solution and see how it does. When you are
finished editing your code, use submit [file] to submit your answer. If your
solution passes the test cases, it will be removed from your home folder.


CONSTRAINTS
Java
====
Your code will be compiled using standard Java 8. All tests will be run by
calling the solution() method inside the Solution class

Execution time is limited.
Wildcard imports and some specific classes are restricted
(e.g. java.lang.ClassLoader). You will receive an error when you verify your
solution if you have used a blacklisted class.

Third-party libraries, input/output operations, spawning threads or processes
and changes to the execution environment are not allowed.

Your solution must be under 32000 characters in length including new lines and
other non-printing characters.

Python
======
Your code will run inside a Python 2.7.13 sandbox. All tests will be run by
calling the solution() function.

Standard libraries are supported except for bz2, crypt, fcntl, mmap, pwd,
pyexpat, select, signal, termios, thread, time, unicodedata, zipimport, zlib.

Input/output operations are not allowed.

Your solution must be under 32000 characters in length including new lines
and other non-printing characters.
"""

# Apologies for any formatting or styling errors, I have started learning
# programming less than a year ago with Ruby, I have read only one book on
# Python so far so I am not familiar with the style guides

def solution1(data, n):
    if n > 0:
        for x in set(data):
            if data.count(x) > n:
                while x in data:
                    data.remove(x)
        return data
    else:
        return []


from collections import Counter

def solution2(data, n):
    if n > 0:
        histogram = Counter(data)
        return([d for d in data if histogram[d] <= n])
    else:
        return []


def solution3(data, n):
    if n > 0:
        return([d for d in data if data.count(d) <= n])
    else:
        return []

def solution4(data, n):
    if n > 0: 
        occurrences = {}
        for item in data:
            occurrences[item] = occurrences.get(item, 0) + 1
        # return trimmed data
        trimmed_data = []
        for item in data:
            if occurrences[item] <= n:
                trimmed_data.append(item)
        return trimmed_data
    else:
        return []

def solution5(data, n):
    if n > 0:
        occurrences = {}
        # count occurrences
        for item in data:
            occurrences[item] = occurrences.get(item, 0) + 1
        # return trimmed data
        data.clear()
        for k, v in occurrences.items():
            if v <= n:
                data.append(k)
        return data
    else:
        return []

def solution6(data, n):
    lambda data, n: [x for x in set(data) if data.count(x) <= n]


# from collections import OrderedDict

# def solution(list_of_ids, number_of_repetitions):

#     if number_of_repetitions > 0:
        
#     else
#     return [] number_of_repetitions == 1:
#         print list(OrderedDict.fromkeys(list_of_ids))
#     else:
#         for x in set(list_of_ids):
#             if list_of_ids.count(x) > number_of_repetitions:
#                 while x in list_of_ids:
#                     list_of_ids.remove(x)

#         print list_of_ids


#     #print(list_of_ids)

        # recurrence = {}
        # for id in list_of_ids:
        #     recurrence[id] = recurrence.get(id, 0) + 1
        #     list_of_ids.clear()
        #     for key, value in recurrence.ids():
        #         if value < number_of_repetitions:
        #             list_of_ids.append(key)
        #     return list_of_ids
    
    # for id in list_of_ids:
    #     if id < number_of_repetitions:
    #         new_list_of_ids.append(id)

    # print(new_list_of_ids)

    # print(enumerate(list_of_ids))
    # print(map(list_of_ids))
    # print(map(enumerate(list_of_ids)))


    # return list(list_of_ids)


# solution([10, 22, 22, 33, 33, 33, 44, 55, 55], 1)
# solution([10, 22, 33], 0)
# solution([99, 98, 97, 96, 99, 98, 97, 99, 98, 99, 11, 12, 13, 14, 15, 16, 11, 12, 13, 14, 15, 11, 12, 13, 14, 11, 12, 13, 11, 12, 11], 3)

import numpy as np

random_list = list(np.random.randint(low = 1,high=9999999,size=10000000))

#print(solution1(random_list, 2))
print(solution2(random_list, 2))
#print(solution3(random_list, 2))
#print(solution4(random_list, 2)) ?

#print(solution5(random_list, 2))
#print(solution6(random_list, 2))
 