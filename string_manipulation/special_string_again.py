def substrCount(n: int, s: str) -> int:
    count = n
    i = 0

    while i < n:
        repeat = 0
        # Check for repeated characters
        while i < n - 1 and s[i] == s[i + 1]:
            repeat += 1
            i += 1
        i += 1
        # Get special substring combinations from repeated characters
        count += repeat * (repeat + 1) // 2
        idx = 1
        # Check for special case with middle character removal
        while (
            i - idx >= 0
            and i + idx < n
            and s[i - idx] == s[i + idx]
            and s[i - 1] == s[i + idx]
        ):
            count += 1
            idx += 1

    return count


def test(fn) -> None:
    case_0_n = 7
    case_0_s = "abcbaba"
    assert fn(case_0_n, case_0_s) == 10

    case_1_n = 4
    case_1_s = "aaaba"
    assert fn(case_1_n, case_1_s) == 7


if __name__ == "__main__":
    test(substrCount)
