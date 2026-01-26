def alternatingCharacters(s: str) -> int:
    dels = 0
    curr_char = s[0]
    for i in range(1, len(s)):
        # If next character is the same as the current character
        if curr_char == s[i]:
            # Delete the duplicated character
            dels += 1
        # If the next character is a different character
        else:
            # Update the character tracker to the next character
            curr_char = s[i]
    return dels


def test(fn) -> None:
    case_0_s = "AABAAB"
    assert fn(case_0_s) == 2


if __name__ == "__main__":
    test(alternatingCharacters)
