def show_bus_delays(ax, data):
    expected = data["expected_bus_arrival_time"]
    actual = data["actual_arrival_time"]

    expected_minutes = expected.dt.hour * 60 + expected.dt.minute
    actual_minutes = actual.dt.hour * 60 + actual.dt.minute

    data["delay"] = actual_minutes - expected_minutes

    average_delay = data.groupby("bus")["delay"].mean()

    ax.bar(average_delay.index.astype(str), average_delay.values)

    ax.set_title("Average Bus Delays")
    ax.set_xlabel("Bus Route")
    ax.set_ylabel("Minutes Early / Late")
    ax.axhline(0, color="black")
