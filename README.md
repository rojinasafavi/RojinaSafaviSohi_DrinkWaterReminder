# Drink Water & Stretch Reminder

This small Python project displays a popup reminder to **drink water** and **stretch** every 30 minutes.

## Files
- `README.md` – this documentation.
- `GEMINI.md` – instructions for Gemini to generate the script.
- `script.py` – the Python script that shows the reminder.

## Requirements
- Python 3.6+ (tested on Windows 10/11).
- The standard library `tkinter` (included with most Python installations).

## Installation
1. Clone or copy the project folder.
2. (Optional) Create a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
3. Install any dependencies (none required beyond the standard library).

## Usage
Run the script:
```bash
python script.py
```
A popup will appear immediately and then every 30 minutes. Press `Ctrl+C` in the terminal to stop the script.

## Customisation
- To change the interval, edit the `INTERVAL_SECONDS` constant in `script.py`.
- To add a sound, modify `show_reminder()` to play an audio file.
