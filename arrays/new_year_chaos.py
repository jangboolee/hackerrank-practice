def minimumBribes(q: list[int]) -> None:
    bribes = 0
    for i in range(len(q)):
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return

        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribes += 1

    print(bribes)


def test(fn) -> None:
    case_0_q = [1, 2, 3, 5, 4, 6, 7, 8]
    fn(case_0_q)

    case_1_q = [4, 1, 2, 3]
    fn(case_1_q)


if __name__ == "__main__":
    test(minimumBribes)
