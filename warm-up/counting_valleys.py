def countingValleys(steps: int, path: str) -> int:
    def find_valley(curr: int, step: str, mapper: dict[str, int]) -> bool:
        if curr < 0 and curr + mapper[step] >= 0:
            return True
        return False

    # Initialize counters
    elevation = 0
    valleys = 0
    # Initialize mapper
    mapper = {"D": -1, "U": 1}
    # Track elevation and tally valleys
    for step in path:
        # Check if new step leads to valley
        if find_valley(elevation, step, mapper):
            valleys += 1
        # Update elevation tracker
        elevation += mapper[step]

    return valleys


def test(fn) -> None:
    case_0_steps, case_0_path = (8, "UDDDUDUU")
    assert fn(case_0_steps, case_0_path) == 1

    case_1_steps, case_1_path = (12, "DDUUDDUDUUUD")
    assert fn(case_1_steps, case_1_path) == 2


if __name__ == "__main__":
    test(countingValleys)
