from typing import List


# This method should:
# Return the fewest number of bills possible to make change for the amount
# passed in given the denominations you can make change with.
#
# amount: The amount of money passed in to make change for denominations:
# The bills you can use to make change.  IE: 1s, 5s, 10s, 20s, etc.
#
# Other info:
# You will always be given denominations that will be able to make even change
# (no remainders). Only positive amounts and positive denominations will be
# passed in. Neither the amount nor the denominations will ever be null.
# The amount will always be greater than 0.
def make_change(amount: int, denominations: List[int]) -> dict:

    coin_numbers = {}

    denominations.sort(reverse=True)
    remaining_amount = amount

    while remaining_amount > 0:
        for denomination in denominations:
            while remaining_amount - denomination >= 0:
                remaining_amount = remaining_amount - denomination

                if denomination not in coin_numbers:
                    coin_numbers[denomination] = 1

                else:
                    coin_numbers[denomination] = coin_numbers[denomination] + 1

    return coin_numbers


# change for $55 should be 2:20s, 1:10, and 1:5
results = make_change(55, [5, 10, 1, 20])
assert results.get(20) == 2
assert results.get(10) == 1
assert results.get(5) == 1

# change for $33 should be 6:5s and 3:1s
results = make_change(33, [1, 5])
assert results.get(5) == 6
assert results.get(1) == 3

# change for $104 should be 2:50s and 4:1s
results = make_change(104, [1, 10, 5, 50, 20])
assert results.get(50) == 2
assert results.get(1) == 4



