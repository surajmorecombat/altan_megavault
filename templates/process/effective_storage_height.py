def calculate_effective_storage_height(max_storage_height,min_storage_height):
    effective_storage_height = (max_storage_height + min_storage_height) / 2
    return round(effective_storage_height, 3)

if __name__ == "__main__":
    print("Effective Storage Height Calculator")

    max_height = float(input("Enter Max Storage Height: "))
    min_height = float(input("Enter Min Storage Height: "))

    result = calculate_effective_storage_height(max_height, min_height)

    print("Effective Storage Height:", result)


# def calculate_effective_storage_height(max_storage_height, min_storage_height):
#     return (max_storage_height + min_storage_height) / 2