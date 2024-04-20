import os
import tkinter as tk
from tkinter import simpledialog
import time
import csv
from datetime import datetime

class WorkTimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Client Work Tracker")
        self.root.geometry("400x200")  # Set the window size
        self.root.resizable(False, False)  # Disable resizing

        self.start_time = None
        self.end_time = None
        self.working = False

        self.client_button = tk.Button(self.root, text="Holiday Inn Stuttgart", command=self.toggle_work_session)
        self.client_button.pack(pady=20)

        self.session_label = tk.Label(self.root, text="")
        self.session_label.pack(pady=10)

    def toggle_work_session(self):
        if not self.working:
            self.start_work()
        else:
            self.end_work()
            description = simpledialog.askstring("Input", "Describe the work performed:", parent=self.root)
            # Save to CSV
            self.save_session(self.start_time, self.end_time, self.duration, description)

    def start_work(self):
        self.start_time = time.time()
        self.working = True
        self.client_button.config(text="End Work")
        self.session_label.config(text="Work session in progress...")

    def end_work(self):
        self.end_time = time.time()
        self.working = False
        self.duration = self.end_time - self.start_time
        self.client_button.config(text="Holiday Inn Stuttgart")
        self.session_label.config(text="")

    def save_session(self, start, end, duration, description):
        directory = os.path.join("..", "Data")
        filename = "holiday_inn_stuttgart_hours.csv"
        filepath = os.path.join(directory, filename)

        if not os.path.exists(directory):
            os.makedirs(directory)

        with open(filepath, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([datetime.fromtimestamp(start).strftime('%Y-%m-%d %H:%M:%S'),
                             datetime.fromtimestamp(end).strftime('%Y-%m-%d %H:%M:%S'),
                             f"{duration:.2f} seconds",
                             description])

        print("Session saved successfully.")

if __name__ == "__main__":
    root = tk.Tk()
    app = WorkTimerApp(root)
    root.mainloop()
