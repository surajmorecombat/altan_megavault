def calculate_volume_per_module(internal_height):
    """
    Excel BR45
    """
    return 8.277 + (internal_height - 1) * 10 * 0.827 + (0.26 * 0.26 * internal_height * 2)


def calculate_effective_volume_per_module(volume_per_module, internal_height, effective_storage_height):
    """
    Excel BR46
    """
    return (volume_per_module / internal_height) * effective_storage_height


def calculate_proposed_effective_volume(
    selected_modules,
    effective_volume_per_module,
    filter_volume,
    head_chamber
):
    """
    Excel Proposed Effective Volume
    """

    if head_chamber.lower() == "yes":
        proposed_volume = (
            selected_modules * effective_volume_per_module
        ) - effective_volume_per_module - filter_volume
    else:
        proposed_volume = (
            selected_modules * effective_volume_per_module
        ) - filter_volume

    return proposed_volume


if __name__ == "__main__":

    print("Proposed Effective Volume Calculator")
    print("------------------------------------")

    selected_modules = int(input("Selected Modules: "))
    internal_height = float(input("Internal Megavault Height (m): "))
    effective_storage_height = float(input("Effective Storage Height (m): "))
    filter_volume = float(input("Subsurface Filter Bay Volume (kL): "))
    head_chamber = input("Additional Module for Head Chamber (Yes/No): ")

    volume_per_module = calculate_volume_per_module(internal_height)

    effective_volume_per_module = calculate_effective_volume_per_module(
        volume_per_module,
        internal_height,
        effective_storage_height
    )

    proposed_effective_volume = calculate_proposed_effective_volume(
        selected_modules,
        effective_volume_per_module,
        filter_volume,
        head_chamber
    )

    print("\nVolume Per Module:", round(volume_per_module, 3))
    print("Effective Volume Per Module:", round(effective_volume_per_module, 4))
    print("Proposed Effective Volume (kL):", round(proposed_effective_volume, 2))