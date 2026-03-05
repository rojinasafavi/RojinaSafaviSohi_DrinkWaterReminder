# GEMINI Instructions

The following describes how Gemini should generate the `script.py` for the water and stretch reminder project.

## Requirements
- Use the Python standard library only.
- Use `tkinter` to display a popup message box.
- The popup should have the title **"Hydration & Stretch Reminder"** and the message **"Time to drink water and stretch!"**.
- The reminder should trigger immediately when the script starts and then repeat every **30 minutes**.
- Implement the interval using a constant `INTERVAL_SECONDS = 30 * 60` (seconds). For quick testing, you may temporarily set this to a smaller value (e.g., `5` seconds).
- The script should run indefinitely until the user stops it with `Ctrl+C`.
- Use a background thread so the main thread can keep the process alive.

## Desired File Structure
```
RojinaSafaviSohi_DrinkWaterReminder/
├─ README.md
├─ GEMINI.md
└─ script.py
```

## Example Usage
```bash
python script.py
```
Running the script should open a popup immediately and then every interval.

## Notes
- No external dependencies are required; `tkinter` is included with most Python installations on Windows.
- Ensure the script works on Windows 10/11.
- Provide clear comments in the generated code.
