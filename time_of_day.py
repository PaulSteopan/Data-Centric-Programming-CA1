
def show_time_of_day(ax, data):
    hours = (
        data["expected_bus_arrival_time"].dt.hour
        + data["expected_bus_arrival_time"].dt.minute / 60
    )

    durations = data["duration_of_trip(min)"]

    ax.scatter(hours, durations)

    ax.set_title("Arrival Time and Journey Duration")
    ax.set_xlabel("Scheduled Arrival Time")
    ax.set_ylabel("Journey Duration (minutes)")

    ax.set_xticks([6, 9, 12, 15, 18, 21])
    ax.set_xticklabels([
        "06:00", "09:00", "12:00",
        "15:00", "18:00", "21:00"
    ])

    ax.grid(True)
