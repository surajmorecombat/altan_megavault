MODULE_WIDTH = 2.402

def calculate_tank_width(grid):
    """
    Replicates Excel logic:
    MAX(SUM(column)) * 2.402
    """

    # transpose grid to read columns
    column_sums = [sum(col) for col in zip(*grid)]

    max_modules_in_column = max(column_sums)

    tank_width = max_modules_in_column * MODULE_WIDTH

    return tank_width


if __name__ == "__main__":

    print("Tank Width Calculator")
    print("---------------------")

    grid = [
        [1,1,1,1,1],
        [1,1,1,0,0],
        [1,1,0,0,0],
        [1,1,1,1,0]
    ]

    width = calculate_tank_width(grid)

    print("Tank Width (m):", round(width,2))