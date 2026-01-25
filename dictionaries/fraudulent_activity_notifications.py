def activityNotifications(expenditure: list[int], d: int):
    notices = 0
    max_expenditure = 200

    # Initialize a frequency array for the last d days
    count = [0] * (max_expenditure + 1)
    # Populate the frequency array with the first d days
    for exp in expenditure[:d]:
        count[exp] += 1

    def find_median(count, d):
        total = 0
        if d % 2 == 0:
            first_median = second_median = None
            for i in range(len(count)):
                total += count[i]
                if total >= d // 2 and first_median is None:
                    first_median = i
                if total >= d // 2 + 1 and second_median is None:
                    second_median = i
                    break
            return (first_median + second_median) / 2
        else:
            for i in range(len(count)):
                total += count[i]
                if total > d // 2:
                    return i

    # Process each day starting from day d
    for i in range(d, len(expenditure)):
        # Find the current median
        median_value = find_median(count, d)
        # Check for a notification
        if expenditure[i] >= 2 * median_value:
            notices += 1
        # Add current day's expenditure to frequency array
        count[expenditure[i]] += 1
        # Remove the expenditure from d days ago
        count[expenditure[i - d]] -= 1

    return notices


def test(fn) -> None:
    case_0_expenditure = [10, 20, 30, 40, 50]
    case0_d = 3
    assert fn(case_0_expenditure, case0_d) == 1


if __name__ == "__main__":
    test(activityNotifications)
