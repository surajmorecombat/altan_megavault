def calculate_effective_volume_per_base(
    total_volume_per_base,
    internal_height,
    effective_storage_height
):

    effective_volume = (
        total_volume_per_base / internal_height
    ) * effective_storage_height

    return effective_volume

if __name__ == "__main__":
    print("Effective Volume Per Base Unit Calculator")
    print("------------------------------------------")

    total_volume_per_base = float(input("Enter Total Volume Per Base Unit (BR45): "))
    internal_height = float(input("Enter Internal Megavault Height (B9): "))
    effective_storage_height = float(input("Enter Effective Storage Height (B10): "))

    result = calculate_effective_volume_per_base(total_volume_per_base,
        internal_height,
        effective_storage_height)
    print("\nEffective Volume Per Base Unit (kL):", round(result, 4))

