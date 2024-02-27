# N-Queens CSP
## Overview
Write a program that solves N-Queen in n*n grid.   Start with a random board, with one queen in each column.  Use iterative search algorithm.

Constraints:  10 <= n <= 1000

Input Format: A file with n lines; each line has the column location of the i-th row’s queen. Read the comments in the sample file. You have n-queen.txt as a sample file. You code should work with any n.

Algorithm
Write a CSP algorithm to solve this problem.  The CSP algorithm should have the following components:

Search algorithm to solve the CSP
Heuristics (min remaining values, least constraining value, tie breaking rules)
Constraint propagation using AC3.

![4-queens](/pic/4-queens.png)
## Heuritic
### MRV
The MRV heuristic selects the next variable to assign a value to, based on the smallest number of remaining legal values in its domain. The rationale behind MRV is to choose the variable that is most constrained but still has a possibility to find a legal value, thereby possibly reducing the chances of a failure sooner and pruning the search space effectively.
### LCV
Once a variable is chosen for assignment (often using MRV), the LCV heuristic determines the order in which values from its domain are tried. LCV selects the value that imposes the fewest constraints on the remaining unassigned variables, i.e., the value that leaves the maximum number of options open for the other variables.
### Tie-Breaking Rules
Tie-breaking rules are used when the application of MRV, LCV, or other heuristics results in a tie, meaning there are multiple equally good choices for the next step. These rules are additional strategies to decide among the tied options, aiming to further optimize the search process. Common tie-breakers include, but are not limited to:

## Propagations - AC3
AC3 works by iteratively removing values from the domains of variables that are inconsistent with the constraints until all variables have domains containing only consistent values. Here's a step-by-step overview of how the algorithm operates:
## Search Algorithm
### State Space
board: An N-length list of ints: board[N][N]  
queen position: board[row].   
the index of the list represents the row, and the value at each index represents the queen's column in that row.

### Constriants Representation
For every queen position(row, col), make sure board[i] when does not repeat. 
### Conflict Detections

For any given queen, the script counts how many queens it is in conflict with. This includes queens in the same column and diagonals. The count_conflicts function calculates this by comparing the positions of all pairs of queens.

The script iteratively looks for the queen with the most conflicts. In a situation where multiple queens have the same highest number of conflicts, one is randomly selected. This is where the script starts its process of "repairing" the board configuration to reduce conflicts.

### Choose a new position
Once a highly conflicted queen is identified, the script attempts to find a new column for this queen where the number of conflicts is minimized. It does this by:
1. Temporarily "removing" the queen from the board (ignoring its current column).
2. Checking all possible columns in the queen's row to find the column with the fewest conflicts.
3. If multiple columns have the same, minimized number of conflicts, one is chosen at random.

### Iteration
The script repeats the process of selecting the most conflicted queen and minimizing its conflicts by moving it to a better position. This process is repeated for a maximum number of iterations or until a solution is found where no queens conflict with each other.
Max Iterations: The script has a limit (max_iterations) on how many times it will attempt to repair the board. This prevents it from running indefinitely in case a solution isn't found.