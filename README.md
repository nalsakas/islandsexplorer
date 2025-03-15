# islandsexplorer
For any given mxn matrix of islands, delete islands that don't touch the corners. 

# Problem Statement:
For any given nxm matrix of islands, 1s represents soil nad 0s represents water. Delete islands that have no connection to corners.
If an island touches any corner (left-right-top-bottom) preserve it, else delete it.
```
Input:
[
[1, 0, 0, 0, 0, 0],
[0, 1, 0, 1, 1, 1],
[0, 0, 1, 0, 1, 0],
[1, 1, 0, 0, 1, 0],
[1, 0, 1, 1, 0, 0],
[1, 0, 0, 0, 0, 1]
]

Output:
[
[1, 0, 0, 0, 0, 0],
[0, 0, 0, 1, 1, 1],
[0, 0, 0, 0, 1, 0],
[1, 1, 0, 0, 1, 0],
[1, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 1]
]
```
# Solution:
- Loop over all cells
- Check if that cell touches a corner or not
- Implement a dfs algorithm to figure out whether an island/cell (conected cells with value of 1s) touches any corner
- Implement a dfs algorithm to delete an island/cell (conected cells with value of 1s)
