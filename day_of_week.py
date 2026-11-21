def show_day_of_week(ax, data):
    average_duration = data.groupby("day_of_week")[
        "duration_of_trip(min)"
    ].mean()

    days = [
        "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"
    ]

    average_duration = average_duration.reindex(days)

    ax.bar(average_duration.index, average_duration.values)

    ax.set_title("Average Journey Duration by Day")
    ax.set_xlabel("Day of the Week")
    ax.set_ylabel("Average Minutes")
    ax.tick_params(axis="x", rotation=30)
