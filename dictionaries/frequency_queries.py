from collections import defaultdict


def freqQuery(queries: list[tuple[int, int]]) -> list[int]:
    output = []
    # Maintain hash map of item count
    freqs = defaultdict(int)
    for operation, item in queries:
        if operation == 1:
            # Insert into data structure
            freqs[item] += 1
        elif operation == 2:
            # Delete one occurence of item
            if item in freqs.keys():
                # Ensure minimum count is 0
                if freqs[item] > 0:
                    freqs[item] -= 1
        else:
            # Check for exact frequency of item
            unique_freqs = set(freqs.values())
            if item in unique_freqs:
                output.append(1)
            else:
                output.append(0)

    return output


def test(fn) -> None:
    case_0_queries = [(1, 1), (2, 2), (3, 2), (1, 1), (1, 1), (2, 1), (3, 2)]
    assert fn(case_0_queries) == [0, 1]


if __name__ == "__main__":
    test(freqQuery)
