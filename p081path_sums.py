import sys
'''
example matrix

131 763 234 103  18
201  96 342 965 150
630 803 746 422 111
537 699 497 121 956
805 732 524  37 331
-------------------

idea #1. bruteforce. check all top-left to bottom-right paths sums
moving right and down and find the minimum. this is of course is not
feasible for problems of large sizes due to the exponential growth of
the running time of the recursive algorithm.

idea #2. dynamically. as is usual with dynamic solutions, thing as though
you are starting from the end! starting from bottom right, that cell
was reachead via either the cell right above it or the cell to the
left of it. thus the minimal 'cost' of reaching that cell is the cost
of that cell itself plus the minimum of the two cells. thus if we let a[i][j]
denote the 'cost' of reaching cell ij, we arrive at the recurrence relation:

case1:  i = 0  i = 0   a[i][j]  = a[i][j]
case2:  i = 0  j > 0   a[i][j] += a[i][j-1]
case3:  i > 0  j = 0   a[i][j] += a[i-1][j]
case4:  i > 0  j > 0   a[i][j] += min(a[i-1][j], a[i][j-1])
'''
def min_sum_path(a):
    m = len(a)
    n = len(a[0])
    #case 1: trivial

    #case 2: i = 0  j > 0
    for j in range(1, n): a[0][j] += a[0][j-1]

    #case 3: i > 0 j = 0
    for i in range(1, m): a[i][0] += a[i-1][0]

    # case 4: i > 0 j > 0
    for i in range(1, m):
        for j in range(1, n):
            a[i][j] += min(a[i-1][j], a[i][j-1])
    return a[m-1][n-1]

if __name__ == '__main__':
    # read input matrix
    a = []
    for line in sys.stdin:
        line = line.strip().split(',')
        tem  = [int(x) for x in line]
        a.append(tem)

    print(min_sum_path(a))
