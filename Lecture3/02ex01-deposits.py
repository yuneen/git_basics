#!/usr/bin/env python3

"""Calculate deposit percent yield based on time period.

Imagine your friend wants to put money on a deposit.
He has got many offers from different banks:
- First bank declares +A% each day;
- Second bank promises +B% each month;
- Third bank offers +C% by the end of the year;
- The 4th bank promotes +D% in a 10-year term;
- ... and so on ...

Your friend gets a terrible headache calculating all this stuff,
and asks you to help checking everything. You quickly realize
it is a common task and having a simple script is a great idea.

Let's implement this.

A simplified task:
Given the SUM amount of money, and PERCENT yield promised in a
FIXED_PERIOD of time, calculate the TOTAL equivalent of money
in a SET_PERIOD of time.

Math formula:
p = PERCENT / 100
TOTAL = SUM * ((1 + p) ** (SET_PERIOD / FIXED_PERIOD))
"""


# TODO: (extra) Output only percents if the initial SUM is
#       not known at the moment the script is run


USAGE = """USAGE: {script} initial_sum percent fixed_period set_period

\tCalculate deposit yield. See script source for more details.
"""
USAGE = USAGE.strip()


def deposit(initial_sum, percent, fixed_period, set_period):
    """Calculate deposit yield."""
    per = percent / 100
    growth = round((1 + per) ** (set_period / fixed_period), 2)
    growth_m = round((1 + per) ** (30 / fixed_period), 2)
    growth_y = round((1 + per) ** (365 / fixed_period), 2)
    growth_5 = round((1 + per) ** (1826 / fixed_period), 2)
    growth_10 = round((1 + per) ** (3652 / fixed_period), 2)
    year_per = round((growth_y - 1)* 100, 2)

    return initial_sum * growth, initial_sum * growth_m, initial_sum * growth_y, initial_sum * growth_5, initial_sum * growth_10, year_per
    


def main(args):

    """Gets called when run as a script."""
    if len(args) != 4 + 1:
        exit(USAGE.format(script=args[0]))

    args = args[1:]
    initial_sum, percent, fixed_period, set_period = map(float, args)

    # same as
    # initial_sum = float(args[0])
    # percent = float(args[1])
    # ...

    res = deposit(initial_sum, percent, fixed_period, set_period)
    print(res)


if __name__ == '__main__':
    import sys

    main(sys.argv)
