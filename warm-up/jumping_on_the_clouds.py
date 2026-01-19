def jumpingOnClouds(c: list[int]) -> int:
    i = 0
    jumps = 0

    while i < len(c) - 1:
        # If on the second last cloud
        if i == len(c) - 2:
            # Always jump once to the final cloud
            i += 1
            jumps += 1
        # For all other clouds
        else:
            # Check two clouds over
            plus_2 = c[i + 2]
            # Jump once only if two clouds over is a thunderhead
            if plus_2 == 1:
                i += 1
            # Always jump two clouds if possible
            else:
                i += 2
            jumps += 1

    return jumps


def test(fn) -> None:
    case_0_c = [0, 1, 0, 0, 0, 1, 0]
    assert fn(case_0_c) == 3

    case_1_c = [0, 0, 0, 1, 0, 0]
    assert fn(case_1_c) == 3


if __name__ == "__main__":
    test(jumpingOnClouds)
