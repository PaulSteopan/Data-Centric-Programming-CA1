def show_journey_direction(ax, data):
    data["direction"] = (
        data["departure_location"] + " to " + data["arrival_location"]
    )

    average_duration = data.groupby("direction")[
        "duration_of_trip(min)"
    ].mean()

    ax.bar(average_duration.index, average_duration.values)

    ax.set_title("Average Journey Duration by Direction")
    ax.set_xlabel("Journey Direction")
    ax.set_ylabel("Average Minutes")
    ax.tick_params(axis="x", rotation=20)
