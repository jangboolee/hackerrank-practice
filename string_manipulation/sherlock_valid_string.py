from collections import Counter


def isValid(s: str) -> str:
    # Create dictionary of character counts
    chars = Counter(s)
    # Create dictionary of frequencies of counts
    freqs = Counter(chars.values())
    # If there is only one count
    if len(freqs) == 1:
        # Valid string as-is
        return "YES"
    # If there are two counts
    if len(freqs) == 2:
        # Get frequencies and counts
        freq1, freq2 = freqs.items()
        (count1, a), (count2, b) = (freq1), (freq2)
        # If there is one character to delete
        if min(freqs.values()) == 1:
            # If there is one instance of the one character
            if (count1 == 1 and a == 1) or (count2 == 1 and b == 1):
                # Valid after removing the single instance
                return "YES"
            # If the min count and max count differ by 1
            if abs(count1 - count2) == 1:
                return "YES"
    # Invalid otherwise
    return "NO"


def test(fn) -> None:
    case_0_s = "abcdefghhgfedecba"
    assert fn(case_0_s) == "YES"

    case_1_s = "aaaabbcc"
    assert fn(case_1_s) == "NO"


if __name__ == "__main__":
    test(isValid)
