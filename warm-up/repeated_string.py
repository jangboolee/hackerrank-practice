def repeatedString(s: str, n: int) -> int:
    # Count instances of 'a' in s
    a_count = s.count("a")
    # Find instances of repetition
    reps = n // len(s)
    # Find instances of 'a' in trailing characters
    trailing = s[: n % len(s)]
    trailing_a_count = trailing.count("a")
    # Return total instances of 'a'
    return a_count * reps + trailing_a_count


def test(fn) -> None:
    case_0_s, case_0_n = ("aba", 10)
    assert fn(case_0_s, case_0_n) == 7

    case_1_s, case_1_n = ("a", 1000000000000)
    assert fn(case_1_s, case_1_n) == 1000000000000


if __name__ == "__main__":
    test(repeatedString)
