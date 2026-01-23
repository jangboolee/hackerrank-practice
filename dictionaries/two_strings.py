def twoStrings(s1: str, s2: str) -> str:
    s1_chars = set(s1)
    s2_chars = set(s2)
    common_chars = s1_chars & s2_chars

    return "YES" if common_chars else "NO"


def test(fn) -> None:
    case_0_s1 = "and"
    case_0_s2 = "art"
    assert fn(case_0_s1, case_0_s2) == "YES"

    case_0_s1 = "hi"
    case_0_s2 = "world"
    assert fn(case_0_s1, case_0_s2) == "NO"


if __name__ == "__main__":
    test(twoStrings)
