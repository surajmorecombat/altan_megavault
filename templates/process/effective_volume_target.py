import math


def calculate_total_volume_per_base(internal_height):
    """
    Excel:
    BR45 = 8.277 + (B9-1)*10*0.827 + (0.26*0.26*B9*2)
    """

    total_volume = 8.277 + (internal_height - 1) * 10 * 0.827 + (0.26 * 0.26 * internal_height * 2)

    return total_volume


def calculate_effective_volume_per_base(total_volume, internal_height, effective_storage_height):
    """
    Excel:
    BR46 = (BR45 / B9) * B10
    """

    effective_volume = (total_volume / internal_height) * effective_storage_height

    return effective_volume


def calculate_modules_required(target_volume, effective_volume, head_chamber):
    """
    Excel:
    =IF(B16="Yes", ROUNDUP((B8)/BR46,0)+1,
                     ROUNDUP((B8)/BR46,0))
    """

    modules = math.ceil(target_volume / effective_volume)

    if head_chamber.lower() == "yes":
        modules += 1

    return modules


if __name__ == "__main__":

    print("Megavault Module Calculator")
    print("--------------------------------")

    target_volume = float(input("Target Effective Volume (kL): "))
    internal_height = float(input("Internal Megavault Height (m): "))
    effective_storage_height = float(input("Effective Storage Height (m): "))
    head_chamber = input("Additional Module for Head Chamber? (Yes/No): ")

    # Step 1
    total_volume_per_base = calculate_total_volume_per_base(internal_height)

    # Step 2
    effective_volume_per_base = calculate_effective_volume_per_base(
        total_volume_per_base,
        internal_height,
        effective_storage_height
    )

    # Step 3
    modules_required = calculate_modules_required(
        target_volume,
        effective_volume_per_base,
        head_chamber
    )

    print("\nResults")
    print("-------------------------")
    print("Total Volume Per Base:", round(total_volume_per_base, 3))
    print("Effective Volume Per Base:", round(effective_volume_per_base, 3))
    print("Modules Required:", modules_required)