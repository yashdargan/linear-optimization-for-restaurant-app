from collections import defaultdict

import streamlit as st


def price_stamp(stamp):
    prices = defaultdict(int)
    range = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]

    stamp = sorted(stamp)

    for price in stamp:
        label = next(
            (
                f"{prev}-{curr}"
                for prev, curr in zip([0] + range, range)
                if prev <= price < curr
            ),
            f"{range[-1]}+",
        )

        prices[label] += 1

    return prices
