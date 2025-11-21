import subprocess
import tkinter as tk
from tkinter import messagebox

def open_applications(app_paths):
    """Open multiple applications given their executable paths."""
    for path in app_paths:
        try:
            subprocess.Popen(path,shell=True)
        except FileNotFoundError:
            print(f"Application not found: {path}")

if __name__ == "__main__":
    # List of application paths (update as needed)
    apps = [
        r"C:\Users\pradeepda\tools\npp.8.7.7.portable.x64\npp.8.7.7.portable.x64\notepad++.exe",
        r'"C:\Program Files\Google\Chrome\Application\chrome.exe" --profile-directory="Default"',  # Example: Calculator
        r'"C:\Program Files\Google\Chrome\Application\chrome.exe" --profile-directory="Profile 2"',  # Example: Chrome
        r'"C:\Program Files\Google\Chrome\Application\chrome.exe" --profile-directory="Profile 4"',  # Example: Chrome
        r"C:\Users\pradeepda\AppData\Roaming\Zoom\bin\Zoom.exe", #zoom
        r"C:\Users\pradeepda\AppData\Local\Microsoft\WindowsApps\ms-teams.exe",
        r"C:\Users\pradeepda\AppData\Local\Microsoft\WindowsApps\Slack.exe",
        r'"C:\Program Files (x86)\Microsoft\Edge\Application\msedge_proxy.exe"  --profile-directory=Default --app-id=faolnafnngnfdaknnbpnkhgohbobgegn --app-url=https://outlook.office.com/mail/ --app-launch-source=4',
        r"C:\Users\pradeepda\tools\VSCode-win32-x64-1.100.0\Code.exe"
    ]
    
    open_applications(apps)