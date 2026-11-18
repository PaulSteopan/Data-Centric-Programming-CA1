import pandas as pd
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Read the CSV file
data = pd.read_csv(
    "personal public transport.csv",
    encoding="utf-8-sig",
    sep=None,
    engine="python"
)

# Convert arrival times into minutes
expected = pd.to_datetime(
    data["expected_bus_arrival_time"].astype(str).str.strip(),
    format="mixed"
)

actual = pd.to_datetime(
    data["actual_arrival_time"].astype(str).str.strip(),
    format="mixed"
)

# Calculate the difference between arrival times
expected_minutes = expected.dt.hour * 60 + expected.dt.minute
actual_minutes = actual.dt.hour * 60 + actual.dt.minute

data["delay"] = abs(actual_minutes - expected_minutes)

# Calculate the average difference for each bus route
average_delays = data.groupby("bus")["delay"].mean()

routes = average_delays.index.astype(str).tolist()
minutes = average_delays.tolist()


# Create the main window
root = tk.Tk()
root.title("Bus Travel Times")
root.geometry("900x600")

# Create the tabs
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")


# TAB 1 - BUS DELAYS
frame1 = tk.Frame(notebook)
notebook.add(frame1, text="Bus Delays")

label1 = tk.Label(
    frame1,
    text="Average Bus Delay by Route",
    font=("Arial", 16)
)
label1.pack(pady=10)

# Create the graph
fig = Figure(figsize=(7, 4))
ax = fig.add_subplot(111)

ax.bar(routes, minutes)

ax.set_xlabel("Bus Route")
ax.set_ylabel("Average Delay (Minutes)")
ax.set_title("Average Bus Delay by Route")
ax.set_ylim(bottom=0)

# Display the graph
canvas = FigureCanvasTkAgg(fig, master=frame1)
canvas.draw()
canvas.get_tk_widget().pack()


# TAB 2 - JOURNEY DIRECTION
frame2 = tk.Frame(notebook)
notebook.add(frame2, text="Journey Direction")

label2 = tk.Label(
    frame2,
    text="Which direction has the longest average journey duration?"
)
label2.pack(pady=20)


# TAB 3 - DAY OF THE WEEK
frame3 = tk.Frame(notebook)
notebook.add(frame3, text="Day of the Week")

label3 = tk.Label(
    frame3,
    text="Do journey times change depending on the day of the week?"
)
label3.pack(pady=20)


# TAB 4 - TIME OF DAY
frame4 = tk.Frame(notebook)
notebook.add(frame4, text="Time of Day")

label4 = tk.Label(
    frame4,
    text="Are bus journeys longer at certain times of the day?"
)
label4.pack(pady=20)


root.mainloop()
