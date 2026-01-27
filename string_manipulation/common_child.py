def commonChild(s1: str, s2: str) -> int:
    m, n = len(s1), len(s2)
    # Initialize matrix of size (m+1)*(n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    # Build up bottom-up dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


def test(fn) -> None:
    case_0_s1 = "HARRY"
    case_0_s2 = "SALLY"
    assert fn(case_0_s1, case_0_s2) == 2


if __name__ == "__main__":
    test(commonChild)
