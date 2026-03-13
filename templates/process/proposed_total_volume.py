def calculate_volume_per_module(internal_height):
    """
    Excel:
    BR45 = 8.277 + (B9-1)*10*0.827 + (0.26*0.26*B9*2)
    """

    volume_per_module = 8.277 + (internal_height - 1) * 10 * 0.827 + (0.26 * 0.26 * internal_height * 2)

    return volume_per_module


def calculate_proposed_total_volume(selected_modules, volume_per_module):
    """
    Excel:
    Proposed Total Volume = B20 * BR45
    """

    return selected_modules * volume_per_module


if __name__ == "__main__":

    print("Proposed Total Volume Calculator")
    print("--------------------------------")

    selected_modules = int(input("Enter Selected Number of Modules: "))
    internal_height = float(input("Enter Internal Megavault Height (m): "))

    volume_per_module = calculate_volume_per_module(internal_height)

    proposed_total_volume = calculate_proposed_total_volume(
        selected_modules,
        volume_per_module
    )

    print("\nVolume Per Module:", round(volume_per_module, 3))
    print("Proposed Total Volume (kL):", round(proposed_total_volume, 2))