"""
Fixed test cases for is_retest_due — same pattern as the LeetCode stubs:
the tests are given, the implementation isn't.

Run with: pytest
"""

from datetime import date, timedelta
from logic import is_retest_due

TODAY = date(2026, 9, 20)

TEST_CASES = [
    # (date_solved, needed_help, expected)
    (TODAY - timedelta(days=4), True, True),    # past the 3-day mark, due
    (TODAY - timedelta(days=1), True, False),   # too recent, not due yet
    (TODAY - timedelta(days=3), True, True),    # exactly at the boundary — due
    (TODAY - timedelta(days=10), False, False), # never needed a retest at all
    (TODAY, True, False),                        # solved today, not due
]


def test_is_retest_due_fixed_cases():
    for date_solved, needed_help, expected in TEST_CASES:
        result = is_retest_due(date_solved, needed_help, today=TODAY)
        assert result == expected, (
            f"date_solved={date_solved} needed_help={needed_help} "
            f"expected={expected} got={result}"
        )


def test_is_retest_due_with_completed_retest():
    result = is_retest_due(
        TODAY - timedelta(days=10), True, retest_completed_at=TODAY, today=TODAY
    )
    assert result is False, "should not be due onfce a retest has been completed"


def test_is_retest_due_with_growing_interval():
    # repeat_retests on, interval already grown to 6 days: not due yet if
    # less than 6 days have passed since the last completed retest
    result_not_due = is_retest_due(
        TODAY - timedelta(days=20), True,
        retest_completed_at=TODAY - timedelta(days=3),
        repeat_retests=True, retest_interval_days=6, today=TODAY,
    )
    assert result_not_due is False, "should not be due before the grown interval elapses"

    # same setup, but the full 6-day interval has now passed — due again
    result_due = is_retest_due(
        TODAY - timedelta(days=20), True,
        retest_completed_at=TODAY - timedelta(days=6),
        repeat_retests=True, retest_interval_days=6, today=TODAY,
    )
    assert result_due is True, "should be due again once the grown interval has elapsed"
