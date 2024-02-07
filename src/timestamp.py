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


def map_to_broader_category(category):
    # Lowercase the category for case-insensitive matching
    category = category.lower()

    # Define keywords for each broader category
    keywords = {
        "South Indian": ["south"],
        "North Indian": ["north"],
        "Beverages": ["beverages", "drinks", "coffee", "tea"],
    }

    # Search for keywords in the category name
    for broader_category, keyword_list in keywords.items():
        for keyword in keyword_list:
            if keyword in category:
                return broader_category

    # If no keyword is found, assign it to the "Others" category
    return "Chinese"
