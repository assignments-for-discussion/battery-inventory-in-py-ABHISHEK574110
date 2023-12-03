
def count_batteries_by_health(present_capacities):
    """
    Count the number of batteries in each health category: healthy, exchange, and failed.
    
    Args:
        present_capacities (list): A list of present capacities of batteries.

    Returns:
        dict: A dictionary with the counts of batteries in each health category:
            - "healthy": The number of batteries with SoH above 80%.
            - "exchange": The number of batteries with SoH between 62% and 80%.
            - "failed": The number of batteries with SoH below 62%.
    """

    counts = {
        "healthy": 0,
        "exchange": 0,
        "failed": 0
    }

    for capacity in present_capacities:
        soh = calculate_soh(capacity)
        if soh > 80:
            counts["healthy"] += 1
        elif soh > 62:
            counts["exchange"] += 1
        else:
            counts["failed"] += 1

    return counts



def test_bucketing_by_health():
    print("Counting batteries by SoH...\n")

    # Test case 1: All batteries healthy
    present_capacities = [115, 118, 112, 98, 97, 88]
    counts = count_batteries_by_health(present_capacities)
    assert(counts["healthy"] == 6)
    assert(counts["exchange"] == 0)
    assert(counts["failed"] == 0)

    # Test case 2: All batteries failed
    present_capacities = [50, 45, 38, 32, 27, 24]
    counts = count_batteries_by_health(present_capacities)
    assert(counts["healthy"] == 0)
    assert(counts["exchange"] == 0)
    assert(counts["failed"] == 6)

    # Test case 3: Mixed health categories
    present_capacities = [113, 116, 80, 95, 92, 70, 55, 42, 37]
    counts = count_batteries_by_health(present_capacities)
    assert(counts["healthy"] == 2)
    assert(counts["exchange"] == 4)
    assert(counts["failed"] == 3)

    print("Done counting :)")


if __name__ == '__main__':
    test_bucketing_by_health()
