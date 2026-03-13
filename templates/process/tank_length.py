def calculate_tank_length(grid):
    """
    Replicates Excel logic:
    3.602 * MAX(SUM(row))
    """

    max_modules_in_row = max(sum(row) for row in grid)

    tank_length = 3.602 * max_modules_in_row

    return tank_length


if __name__ == "__main__":

    print("Tank Length Calculator")
    print("----------------------")

    grid = [
        [1,1,1,1,1,1,1],
        [1,1,1,1,1,0,0],
        [1,1,1,1,0,0,0],
        [0,0,0,0,0,0,0]
    ]

    length = calculate_tank_length(grid)

    print("Tank Length (m):", round(length,2))