# SET _ (variable name)__ to be ______ (where the second blank can be filled with any number, string, list, or a value returned from a function).
# Go to line _ (line number)__.
# Print _(variable name or string)__.
# If _(variable name) or (value returned from a function)__ is _greater than/equal to/less than_
#  _(variable name or value returned from a function)__ do { _____ } where ____ in the do { } can be filled with any of the 4 statements.
# Go through your pseudo code and test whether it solves your base case
# Test your pseudo code with other test cases
# Write your code in Python/Javascript.
# Test your code with different cases/scenarios.
import random
import string
import re

arr = random.sample(xrange(100000), 100)

def Bubble_Sort(arr):

    for i in range(len(arr)-1):
       for j in range(len(arr)-1-i):
        if arr[j+1] < arr[j]:
             arr[j], arr[j+1] = arr[j+1], arr[j]
    print arr


Bubble_Sort(arr)