def getMinimumCost(k: int, c: list[int]) -> int:
    # Sort flowers in descending order
    c.sort(reverse=True)
    total = 0
    for i, price in enumerate(c):
        # Calculate price multiplier
        multiplier = 1 + i // k
        # Increment total cost using multiplier
        total += price * multiplier
    return total


def test(fn) -> None:
    case_0_k = 3
    case_0_c = [1, 3, 5, 7, 9]
    assert fn(case_0_k, case_0_c) == 29


if __name__ == "__main__":
    test(getMinimumCost)
