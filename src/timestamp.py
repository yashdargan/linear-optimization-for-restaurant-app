def categorize_shift(timestamp):
    hour = timestamp.hour + 1
    shifts = {
        4: "Night-Morning Shift",
        8: "Morning Shift",
        12: "Noon Shift",
        16: "Afternoon Shift",
        20: "Evening Shift",
        24: "Night Shift",
    }
    return shifts.get(
        min(shifts.keys(), key=lambda x: abs(x - hour)), "Other Shift"
    )
