def minimumAbsoluteDifference(arr: list[int]) -> int:
    # Sort array
    arr_sorted = sorted(arr)
    # Find minimum differences between neighboring pairs
    min_diff = float("inf")
    for i in range(len(arr_sorted) - 1):
        diff = abs(arr_sorted[i] - arr_sorted[i + 1])
        if diff < min_diff:
            min_diff = diff
    return min_diff


def test(fn) -> None:
    case_0_arr = [3, -7, 0]
    assert fn(case_0_arr) == 3


if __name__ == "__main__":
    test(minimumAbsoluteDifference)
