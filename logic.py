"""
Pure logic, kept separate from Flask/DB so it's easy to test in isolation.

This mirrors the "revisit cold after ~3 days" rule already used by hand in
PROGRESS.md: a problem is due for a cold retest if it needed help AND at
least 3 days have passed since it was solved AND it hasn't already been
retested.
"""

from datetime import date


def is_retest_due(date_solved: date, needed_help: bool, today: date = None) -> bool:
    # TODO: implement
    #
    # Rules (same as the fall repo's cold-retest convention):
    # - if needed_help is False, it's never due (nothing to retest)
    # - if needed_help is True, it's due once >= 3 days have passed since
    #   date_solved
    # - `today` defaults to the real current date if not passed in (makes
    #   this testable without mocking the clock)

    if needed_help is False:
        return False

    if needed_help is True:
        difference = today - date_solved
        if difference.days >= 3:
            return True
        else:
            return False