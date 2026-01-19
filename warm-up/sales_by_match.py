def sockMerchant(n: int, ar: list[int]) -> int:
    # Count socks by color
    socks = {}
    for sock in ar:
        if sock not in socks.keys():
            socks[sock] = 1
        else:
            socks[sock] += 1
    # Find number of pairs
    pairs = 0
    for color_id, count in socks.items():
        pairs += count // 2

    return pairs


def test(fn) -> None:
    case_0_n, case_0_ar = (9, [10, 20, 20, 10, 10, 30, 50, 10, 20])
    assert fn(case_0_n, case_0_ar) == 3

    case_1_n, case_1_ar = (10, [1, 1, 3, 1, 2, 1, 3, 3, 3, 3])
    assert fn(case_1_n, case_1_ar) == 4


if __name__ == "__main__":
    test(sockMerchant)
