#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The while loop runs inside the n^3 with a multiplication of n^2; regardless, this all depends on the size of n, which means this is an O(n).


b) This starts off as an O(n) but it begins to multiply the iteration and the loop becomes bigger with the numbers, signifying this is O(nlog(n)).


c) This is a recursive algorithm dependent on bunnies(n).

O(n) because it goes through a process:
    O(1) for return
    O(1) for second return
    but you get O(3n) => O(n)

## Exercise II

Binary Search:

We would start in the middle floor and drop the egg. If the broken = true, we move downward halfway and repeat because we know above this floor (including it) the egg will be broken. If broken = false after we drop it, we move halfway upward and repeat. Repeating until the egg does not break. The run time complexity would be O(log(n)). We halve the floors every time we iterate through.
