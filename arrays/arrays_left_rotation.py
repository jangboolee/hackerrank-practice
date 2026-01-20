def rotLeft(a: list[int], d: int) -> list[int]:
    # Factor with which to shift array
    factor = d % len(a)
    # Find left and right half based on factor
    left = a[factor:]
    right = a[:factor]

    return left + right


def test(fn) -> None:
    case_0_a = [1, 2, 3, 4, 5]
    case_0_d = 4

    assert fn(case_0_a, case_0_d) == [5, 1, 2, 3, 4]


if __name__ == "__main__":
    test(rotLeft)
