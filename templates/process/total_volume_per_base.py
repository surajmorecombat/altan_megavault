def calculate_total_volume_per_base(internal_height):

    volume = (
        8.277
        + (internal_height - 1) * 10 * 0.827
        + (0.26 * 0.26 * internal_height * 2)
    )

    return volume


if __name__ == "__main__":

    print("Total Volume Per Base Unit Calculator")
    print("--------------------------------------")

    internal_height = float(input("Enter Internal Megavault Height (B9): "))

    result = calculate_total_volume_per_base(internal_height)

    print("\nTotal Volume Per Base Unit (kL):", round(result, 4))