def group_consecutive(arr: list[int]) -> str:
    # Sort input array
    arr.sort()
    # Create first subarray of the first element
    curr_group = [arr[0]]
    # Group consective integers into subarrays
    groups = []
    for i in range(1, len(arr)):
        # Create new subarray group
        if arr[i] == arr[i - 1] + 1:
            curr_group.append(arr[i])
        else:
            groups.append(curr_group)
            curr_group = [arr[i]]
    groups.append(curr_group)

    # Convert group of subarrays into a single string
    strings = []
    for group in groups:
        if len(group) == 1:
            strings.append(str(group[0]))
        else:
            strings.append(f"{group[0]}-{group[-1]}")

    return ", ".join(strings)


def test(fn) -> None:
    arr = [1, 4, 3, 2, 7, 9, 8, 12, 0]
    assert fn(arr) == "0-4, 7-9, 12"


if __name__ == "__main__":
    test(group_consecutive)
