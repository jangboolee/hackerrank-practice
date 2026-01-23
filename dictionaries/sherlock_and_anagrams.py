from collections import Counter


def sherlockAndAnagrams(s: str) -> int:
    # Generate all possible substrings
    substrings = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            substrings.append(substring)
    # Count anagram matches within substring pairs
    sorted_ss = ["".join(sorted(ss)) for ss in substrings]
    counts = Counter(sorted_ss)

    return sum(v * (v - 1) // 2 for v in counts.values())


def test(fn) -> None:
    case_0_s = "abba"
    assert fn(case_0_s) == 4

    case_1_s = "abcd"
    assert fn(case_1_s) == 0

    case_2_s = "cdcd"
    assert fn(case_2_s) == 5


if __name__ == "__main__":
    test(sherlockAndAnagrams)
