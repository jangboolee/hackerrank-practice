def minimumSwaps(arr: list[int]) -> int:
    swaps = 0
    i = 0
    while i < len(arr):
        # Find the correct value of the position
        correct_value = i + 1
        # If the position is not correctly sorted
        if arr[i] != correct_value:
            # Find where the element should be
            swap_idx = arr[i] - 1
            # Fix the element position with a single swap
            arr[i], arr[swap_idx] = arr[swap_idx], arr[i]
            swaps += 1
        else:
            i += 1
    return swaps


def test(fn) -> None:
    case_0_q = [7, 1, 3, 2, 4, 5, 6]
    assert fn(case_0_q) == 5

    case_1_q = [4, 3, 1, 2]
    fn(case_1_q) == 3


if __name__ == "__main__":
    test(minimumSwaps)
