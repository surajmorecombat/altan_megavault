def calculate_surface_area(volume_per_module, internal_height, selected_modules):

    surface_1 = 1

    surface_2 = ((volume_per_module / internal_height) * selected_modules) / 2

    surface_3 = (volume_per_module / internal_height) * selected_modules

    surface_4 = surface_3

    return [
        round(surface_1, 2),
        round(surface_2, 2),
        round(surface_3, 2),
        round(surface_4, 2)
    ]


if __name__ == "__main__":

    print("OSD Surface Area Calculator")
    print("---------------------------")

    volume_per_module = float(input("Enter Volume per Module (BR45): "))
    internal_height = float(input("Enter Internal Height (B9): "))
    selected_modules = int(input("Enter Selected Modules (B20): "))

    surfaces = calculate_surface_area(
        volume_per_module,
        internal_height,
        selected_modules
    )

    print("\nSurface Areas:")
    for s in surfaces:
        print(s)