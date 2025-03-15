# Go over each cell to determine whetner it is an corner island or not
# If not then delete it.
def removeIslands(arr):
    r = len(arr)
    c = len(arr[0])

    for i in range(r):
        for j in range(c):
            if not cornerIsland(arr, i, j):
                remove(arr, i, j)
    
    print(arr)

# For islands that touches corners return True, else returns None
# Implements dfs algorithm to find out all connected soils
def cornerIsland(arr, i, j, cache = None):
    # cache previously visited cells.
    if cache is None:
        cache = set()

    # Out of boundry check
    if not 0 <= i <len(arr) or not 0 <= j < len(arr[0]):
        return
    
    # in water check
    if arr[i][j] == 0:
        return

    # previously visited?
    if f"{i}{j}" in cache:
        return
    
    # cache it
    cache.add(f"{i}{j}")

    # on corner check?
    if i == 0 or i == len(arr) - 1 or j == 0 or j == len(arr[0]) - 1:
        return True
    
    left = cornerIsland(arr, i, j - 1, cache)
    right = cornerIsland(arr, i, j + 1, cache)
    top = cornerIsland(arr, i - 1, j, cache)
    bottom = cornerIsland(arr, i + 1, j, cache)

    if left or right or top or bottom:
        return True

# Remove island, implemets dfs algoritms to find out all connected soils
def remove(arr, i, j, cache = None):
    if cache is None:
        cache = set()

    if not 0 <= i <len(arr) or not 0 <= j < len(arr[0]):
        return
    
    if arr[i][j] == 0:
        return

    if f"{i}{j}" in cache:
        return
    
    cache.add(f"{i}{j}")

    # recursively remove soil cells
    left = remove(arr, i, j - 1, cache)
    right = remove(arr, i, j + 1, cache)
    top = remove(arr, i - 1, j, cache)
    bottom = remove(arr, i + 1, j, cache)

    # remove soil
    arr[i][j] = 0


arr = [
[1, 0, 0, 0, 0, 0],
[0, 1, 0, 1, 1, 1],
[0, 0, 1, 0, 1, 0],
[1, 1, 0, 0, 1, 0],
[1, 0, 1, 1, 0, 0],
[1, 0, 0, 0, 0, 1]
]

removeIslands(arr)