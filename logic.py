"""
Pure logic, kept separate from Flask/DB so it's easy to test in isolation.

A problem is due for a cold retest if it needed help AND at
least 3 days have passed since it was solved AND it hasn't already been
retested.

"""

from datetime import date


def is_retest_due(date_solved: date, needed_help: bool, today: date = None) -> bool:
    if needed_help is False:
        return False

    if needed_help is True:
        difference = today - date_solved
        if difference.days >= 3:
            return True
        else:
            return False