def countInversions(arr):
    def merge_sort_and_count(arr):
        if len(arr) <= 1:
            return arr, 0
        mid = len(arr) // 2
        # Recursively split array until single items
        left, left_inv = merge_sort_and_count(arr[:mid])
        right, right_inv = merge_sort_and_count(arr[mid:])
        # Merge and count inversions
        merged, split_inv = merge_and_count(left, right)
        total_inv = left_inv + right_inv + split_inv
        return merged, total_inv

    def merge_and_count(left, right):
        merged = []
        i = j = 0
        inversions = 0

        while i < len(left) and j < len(right):
            # If already in ascending order
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            # If not in order
            else:
                # Merge and count inversions
                merged.append(right[j])
                j += 1
                inversions += len(left) - i

        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged, inversions

    _, total_inversions = merge_sort_and_count(arr)
    return total_inversions


def test(fn) -> None:
    case_0_arr = [2, 4, 1]
    assert fn(case_0_arr) == 2


if __name__ == "__main__":
    test(countInversions)
