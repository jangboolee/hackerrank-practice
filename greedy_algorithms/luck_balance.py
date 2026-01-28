def luckBalance(k: int, contests: list[list[int]]) -> int:
    # Count of total important contests
    imp_count = sum([c[1] for c in contests])
    # Luck of important contests, sorted in ascending order of luck
    sorted_imp_contests = sorted(
        [contest[0] for contest in contests if contest[1] == 1]
    )

    # If Lena can lose more than total count of important contests
    if k >= imp_count:
        # Choose to lose every contest
        return sum([contest[0] for contest in contests])
    # If Lena has to win some important contests
    else:
        # Find minimum number of important contests Lena must win
        min_win = imp_count - k
        # Win bottom k important contests
        spent_luck = sum(sorted_imp_contests[:min_win])
        # Subtract spent luck from total possible luck
        return sum([contest[0] for contest in contests]) - spent_luck * 2


def test(fn) -> None:
    case_0_k = 3
    case_0_contests = [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]
    assert fn(case_0_k, case_0_contests) == 29


if __name__ == "__main__":
    test(luckBalance)
