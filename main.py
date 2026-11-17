
import tkinter as tk
from tkinter import ttk


def main():
    root = tk.Tk()
    root.title("Bus Travel Times")
    root.geometry("800x500")

    notebook = ttk.Notebook(root)
    notebook.pack(expand=True, fill="both")

    # Tab 1 - Bus Delays
    frame1 = ttk.Frame(notebook)
    label1 = ttk.Label(
        frame1,
        text="How early or late do buses arrive compared with their scheduled times?"
    )
    label1.pack(pady=20)

    # Tab 2 - Journey Direction
    frame2 = ttk.Frame(notebook)
    label2 = ttk.Label(
        frame2,
        text="Which direction has the longest average journey duration?"
    )
    label2.pack(pady=20)

    # Tab 3 - Day of the Week
    frame3 = ttk.Frame(notebook)
    label3 = ttk.Label(
        frame3,
        text="Do journey times change depending on the day of the week?"
    )
    label3.pack(pady=20)

    # Tab 4 - Time of Day
    frame4 = ttk.Frame(notebook)
    label4 = ttk.Label(
        frame4,
        text="Are bus journeys longer at certain times of the day?"
    )
    label4.pack(pady=20)

    # Add tabs to the notebook
    notebook.add(frame1, text="Bus Delays")
    notebook.add(frame2, text="Journey Direction")
    notebook.add(frame3, text="Day of the Week")
    notebook.add(frame4, text="Time of Day")

    root.mainloop()


if __name__ == "__main__":
    main()
