from collections import defaultdict


def makeAnagram(a: str, b: str) -> int:
    # Count characters in a
    a_char_counts = defaultdict(int)
    for a_char in a:
        a_char_counts[a_char] += 1
    # Count characters in b
    b_char_counts = defaultdict(int)
    for b_char in b:
        b_char_counts[b_char] += 1
    # Sum count of non-overlapping characters
    total = 0
    for a_char, a_count in a_char_counts.items():
        # Same character exists across both
        if a_char in b_char_counts.keys():
            b_count = b_char_counts[a_char]
            # If count is different
            if a_count > b_count:
                total += a_count - b_count
        # Character in a does not exist in b
        else:
            total += a_count
    for b_char, b_count in b_char_counts.items():
        # Same character exists across both
        if b_char in a_char_counts.keys():
            a_count = a_char_counts[b_char]
            # If count is different
            if b_count > a_count:
                total += b_count - a_count
        # Character in a does not exist in b
        else:
            total += b_count
    return total


def test(fn) -> None:
    case_0_a = "cde"
    case_0_b = "dcf"
    assert fn(case_0_a, case_0_b) == 2


if __name__ == "__main__":
    test(makeAnagram)
