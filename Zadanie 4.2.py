def make_ruler(n):
        top = "|"
        for i in range(n):
            top += "....|"

        bottom = ""
        for i in range(n + 1):
            bottom += f"{i}".ljust(5)

        ruler = top + "\n" + bottom
        return ruler

def make_grid(rows, cols):
    grid = ""
    for i in range(rows):
        for j in range(cols):
            grid += "+---"
        grid += "+\n"
    return grid
ruler1 = make_ruler(12)
ruler2 = make_ruler(20)
ruler3 = make_ruler(5)
grid1 = make_grid(3, 3)
grid2 = make_grid(5, 3)
grid3 = make_grid(3, 5)
print(ruler1 + "\n" + ruler2 + "\n" + ruler3 + "\n")
print(grid1 + "\n" + grid2 + "\n" + grid3 + "\n")