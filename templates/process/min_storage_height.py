def calculate_min_storage_height(max_storage_height, tank_grade_percent, direction):

    # convert percent to decimal
    tank_grade = tank_grade_percent / 100

    if direction in ["→", "←"]:
        tank_length = float(input("Enter Tank Length (m): "))
        min_height = max_storage_height - (tank_grade * tank_length)

    elif direction in ["↑", "↓"]:
        tank_width = float(input("Enter Tank Width (m): "))
        min_height = max_storage_height - (tank_grade * tank_width)

    else:
        raise ValueError("Invalid direction")

    return round(min_height, 3)


if __name__ == "__main__":

    print("Min Storage Height Calculator")
    print("--------------------------------")

    max_height = float(input("Enter Max Storage Height (m): "))
    tank_grade_percent = float(input("Enter Tank Grade (%) : "))
    direction = input("Enter Direction (→ ← ↑ ↓): ")

    result = calculate_min_storage_height(
        max_height,
        tank_grade_percent,
        direction
    )

    print("Min Storage Height (m):", result)