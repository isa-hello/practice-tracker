"""
Pure logic, kept separate from Flask/DB so it's easy to test in isolation.

A problem is due for a cold retest if it needed help AND at
least 3 days have passed since it was solved AND it hasn't already been
retested.

"""

from datetime import date


def is_retest_due(date_solved: date, needed_help: bool, retest_completed_at: date = None,
                  repeat_retests: bool = False, retest_interval_days: int = 3, today: date = None) -> bool:
    if not needed_help:
        return False

    if retest_completed_at is not None and not repeat_retests:
        return False

    last_event_date = retest_completed_at or date_solved
    return (today - last_event_date).days >= retest_interval_days