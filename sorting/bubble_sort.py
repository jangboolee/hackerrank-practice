def countSwaps(a: list[int]) -> tuple[int, int, int]:
    swaps = 0
    for _ in range(len(a)):
        for j in range(0, len(a) - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
    print(f"Array is sorted in {swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")
    return swaps, a[0], a[-1]


def test(fn) -> None:
    case_0_a = [6, 4, 1]
    assert fn(case_0_a) == (3, 1, 6)


if __name__ == "__main__":
    test(countSwaps)
