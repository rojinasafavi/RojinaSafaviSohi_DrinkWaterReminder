import tkinter as tk
from tkinter import messagebox
import threading
import time

INTERVAL_SECONDS = 30 * 60  # 30 minutes

def show_reminder():
    """Displays the reminder popup."""
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Ensure the popup is positioned above other windows
    root.attributes("-topmost", True)
    
    # Show the informational message box
    messagebox.showinfo("Hydration & Stretch Reminder", "Time to drink water and stretch!", parent=root)
    
    # Clean up the Tkinter resources
    root.destroy()

def reminder_loop():
    """Runs continuously, showing the reminder at the specified interval."""
    while True:
        show_reminder()
        time.sleep(INTERVAL_SECONDS)

if __name__ == "__main__":
    print(f"Starting Hydration & Stretch Reminder. Interval: {INTERVAL_SECONDS / 60} minutes.")
    print("Press Ctrl+C to stop.")
    
    # Run the reminder loop in a background daemon thread
    threading.Thread(target=reminder_loop, daemon=True).start()
    
    # Keep the main thread alive to capture KeyboardInterrupt (Ctrl+C)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nReminder stopped.")
