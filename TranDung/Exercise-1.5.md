Exercise 1.5
Below are four faulty programs. Each includes test inputs that result in failure. Answer the
following questions about each program.
    
(a)
findLast
Wrong: i variable run in range (1, length) instead of (0, length)
Modify: for (int i=x.length-1; i >= 0; i--)
    
lastZero
Wrong: Iterate the array from the first element to the last element.
Modify: Iterate the array from the last element to the first element.
    
countPositive
Wrong: Condition if (x[i] >= 0)
Modify: if (x[i] > 0)
    
oddOrPos
Wrong: The condition to determine whether a number is odd or not is that
the remainder divided by 2 equal to 1.
Modify: It must be non-zero.
    
(b)
findLast: x = [2, 3, 5], y = 3
lastZero: x = [2, 3, 5]
countPositive: x = [-2, 2, 3, 5]
oddOrPos: x = [1, 2, 3]

(c)
findLast: x = [2, 3, 5], y = 3
lastZero: x = [0]
countPositive: x = [0, 1, 2]
oddOrPos: x = [-3, 0, 3]
    
(d)
x = [2, 3, 5], y = 1
y does not in x so the results are in an error state, but not a failure.
    