import tkinter as tk
from tkinter import ttk
import time
import winsound

class AlarmClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Alarm Clock App")

        self.alarm_time = tk.StringVar()
        self.alarm_time.set("00:00 AM")

        self.alarm_label = ttk.Label(root, text="Set Alarm Time:", font=("Helvetica", 24))
        self.alarm_label.pack(pady=10)

        self.time_entry = ttk.Entry(root, textvariable=self.alarm_time, font=("Helvetica", 24))
        self.time_entry.pack(pady=10)

        self.set_button = ttk.Button(root, text="Set Alarm", command=self.set_alarm)
        self.set_button.pack(pady=5)

        self.reset_button = ttk.Button(root, text="Reset", command=self.reset_alarm)
        self.reset_button.pack(pady=5)

        self.status_label = ttk.Label(root, text="", font=("Helvetica", 24))
        self.status_label.pack(pady=10)

        self.alarm_is_set = False
        self.update_alarm_status()

    def update_alarm_status(self):
        if self.alarm_is_set:
            self.status_label.config(text="Alarm is set for " + self.alarm_time.get())
        else:
            self.status_label.config(text="No alarm is set")

    def set_alarm(self):
        alarm_time_str = self.alarm_time.get()
        try:
            alarm_time = time.strptime(alarm_time_str, "%I:%M %p")
            current_time = time.localtime()

            if alarm_time.tm_hour > current_time.tm_hour or \
               (alarm_time.tm_hour == current_time.tm_hour and alarm_time.tm_min >= current_time.tm_min):

                self.alarm_is_set = True
                self.update_alarm_status()

                time_to_alarm = (alarm_time.tm_hour - current_time.tm_hour) * 3600 + \
                                (alarm_time.tm_min - current_time.tm_min) * 60

                self.root.after(time_to_alarm * 1000, self.trigger_alarm)
            else:
                self.status_label.config(text="Please enter a future time")

        except ValueError:
            self.status_label.config(text="Invalid time format")

    def trigger_alarm(self):
        winsound.Beep(1000, 2000)  
        self.alarm_is_set = False
        self.update_alarm_status()

    def reset_alarm(self):
        self.alarm_is_set = False
        self.update_alarm_status()

def main():
    root = tk.Tk()
    app = AlarmClockApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
