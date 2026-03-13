def calculate_selected_modules(grid):
    """
    Replicates Excel:
    =SUM(G4:AR55)

    Each '1' represents one module.
    """

    total_modules = 0

    for row in grid:
        total_modules += sum(row)

    return total_modules


if __name__ == "__main__":

    print("Selected Modules Calculator")
    print("--------------------------------")

    rows = int(input("Enter number of grid rows: "))
    cols = int(input("Enter number of grid columns: "))

    grid = []

    for r in range(rows):
        row = []
        for c in range(cols):
            value = int(input(f"Enter value for cell ({r+1},{c+1}) [0 or 1]: "))
            row.append(value)
        grid.append(row)

    modules = calculate_selected_modules(grid)

    print("\nSelected Number of Modules:", modules)