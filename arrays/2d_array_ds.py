def hourglassSum(arr: list[list[int]]) -> int:
    def generate_hourglass(
        arr: list[list[int]], row_i: int, col_i: int
    ) -> list[list[int]]:
        # Generate lists for each row of the hourglass
        top = [
            arr[row_i - 1][col_i - 1],
            arr[row_i - 1][col_i],
            arr[row_i - 1][col_i + 1],
        ]
        mid = [0, arr[row_i][col_i], 0]
        bottom = [
            arr[row_i + 1][col_i - 1],
            arr[row_i + 1][col_i],
            arr[row_i + 1][col_i + 1],
        ]
        return [top, mid, bottom]

    def find_hourglass_sum(hourglass: list[list[int]]) -> int:
        total = 0
        for row in hourglass:
            total += sum(row)

        return total

    # Find bounds of 2D array
    rows = len(arr)
    cols = len(arr[0])

    sums = []
    for row_i in range(1, rows - 1):
        for col_i in range(1, cols - 1):
            # Generate hourglass for the middle point
            hourglass = generate_hourglass(arr, row_i, col_i)
            # Calculate sum of the hourglass
            sums.append(find_hourglass_sum(hourglass))

    return max(sums)


def test(fn) -> None:
    case_0_arr = [
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0],
    ]

    assert fn(case_0_arr) == 19


if __name__ == "__main__":
    test(hourglassSum)
