def calculate_osd_elevations(osd_invert_level, tank_length, tank_grade_percent, internal_height):
    """
    Replicates Excel formulas:

    Row1: A30
    Row2: A30 + (B24 * B11) / 2
    Row3: A30 + (B24 * B11)
    Row4: A30 + B9
    """

    # convert percentage to decimal
    tank_grade = tank_grade_percent / 100

    elevation_1 = osd_invert_level

    elevation_2 = osd_invert_level + (tank_length * tank_grade) / 2

    elevation_3 = osd_invert_level + (tank_length * tank_grade)

    elevation_4 = osd_invert_level + internal_height

    return [
        round(elevation_1, 2),
        round(elevation_2, 2),
        round(elevation_3, 2),
        round(elevation_4, 2)
    ]


if __name__ == "__main__":

    print("OSD Elevation Calculator")
    print("------------------------")

    osd_invert_level = float(input("Enter OSD Invert Level: "))
    tank_length = float(input("Enter Tank Length (m): "))
    tank_grade_percent = float(input("Enter Tank Grade (%): "))
    internal_height = float(input("Enter Internal Megavault Height (m): "))

    elevations = calculate_osd_elevations(
        osd_invert_level,
        tank_length,
        tank_grade_percent,
        internal_height
    )

    print("\nElevations:")
    for e in elevations:
        print(e)