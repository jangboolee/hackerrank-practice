from collections import defaultdict


def countTriplets(arr: list[int], r: int) -> int:
    left_count = defaultdict(int)
    right_count = defaultdict(int)

    # Count occurrences of each number
    for number in arr:
        right_count[number] += 1

    triplet_count = 0
    for num in arr:
        # Move current pointer right by one
        right_count[num] -= 1
        # Check if num can be a middle term
        if num % r == 0:
            left_term = num // r
            right_term = num * r
            # If a valid triple can be formed
            if left_term in left_count and right_term in right_count:
                # Increment by number of possible triples
                triplet_count += (
                    left_count[left_term] * right_count[right_term]
                )
        # Move current number to a potential left term
        left_count[num] += 1

    return triplet_count


def test(fn) -> None:
    case_0_arr = [1, 2, 2, 4]
    case_0_r = 2
    assert fn(case_0_arr, case_0_r) == 2

    case_1_arr = [1, 3, 9, 9, 27, 81]
    case_1_r = 3
    assert fn(case_1_arr, case_1_r) == 6

    case_2_arr = [1, 5, 5, 25, 125]
    case_2_r = 5
    assert fn(case_2_arr, case_2_r) == 4


if __name__ == "__main__":
    test(countTriplets)
