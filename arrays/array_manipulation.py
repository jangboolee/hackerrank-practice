def arrayManipulation(n: int, queries: list[list[int]]) -> int:
    # Initialize difference array
    diff = [0] * n

    # Aapply each query to the difference array
    for a, b, k in queries:
        diff[a - 1] += k
        if b < n:
            diff[b] -= k

    # Accumulate to get actual values and track maximum
    max_val = 0
    current = 0
    for i in range(n):
        current += diff[i]
        if current > max_val:
            max_val = current

    return max_val


def test(fn) -> None:
    case_0_n = 10
    case_0_queries = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]
    assert fn(case_0_n, case_0_queries) == 10


if __name__ == "__main__":
    test(arrayManipulation)
