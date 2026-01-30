from collections import Counter


def maxMin(k: int, arr: list[int]) -> int:
    # Create frequency hashmap: O(n)
    freq = Counter(arr)
    # Can create completely fair subarray if k <= max(freq.values())
    if k <= max(freq.values()):
        return 0

    # If duplicate values can not be returned, first sort the array
    arr.sort()
    # Loop using double pointers to find minimum unfairness
    min_unfairness = float("inf")
    for i in range(len(arr) - k + 1):
        # Create left and right pointers
        left, right = i, i + k - 1
        # Find unfairness of the subarray
        min_val, max_val = arr[left], arr[right]
        unfairness = max_val - min_val
        # Check if unfairness is minimum possible value
        if unfairness < min_unfairness:
            min_unfairness = unfairness

    return min_unfairness


def test(fn) -> None:
    case_0_k = 3
    case_0_arr = [100, 200, 300, 350, 400, 401, 402]
    assert fn(case_0_k, case_0_arr) == 2


if __name__ == "__main__":
    test(maxMin)
