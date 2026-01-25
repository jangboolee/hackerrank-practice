def maximumToys(prices: list[int], k: int) -> int:
    # Create a sorted price list
    sorted_prices = sorted(prices)
    # Find cumulative total
    c_total = 0
    count = 0
    for price in sorted_prices:
        # Stop if no longer able to buy any more
        if c_total + price >= k:
            return count
        # Buy next toy and increment counters
        else:
            c_total += price
            count += 1

    return count


def test(fn) -> None:
    case_0_prices = [1, 2, 3, 4]
    case_0_k = 7
    assert fn(case_0_prices, case_0_k) == 3


if __name__ == "__main__":
    test(maximumToys)
