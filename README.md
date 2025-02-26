# Keylogger

This is a simple keylogger script written in Python that logs keystrokes to a file, automatically installs required packages, and hides the console window during execution. It is intended strictly for educational and ethical use.  

## Features
- **Keystroke Logging:** Captures all keystrokes, including special keys like Enter, Backspace, Tab, and Escape.  
- **Timestamped Logs:** Each keypress is recorded with a timestamp for better tracking.  
- **Console Hiding:** Hides the console window once the script starts running.  
- **Automatic Dependency Installation:** Checks for and installs missing packages (`pynput` and `pywin32`).  

## Installation

**Clone the repository:**  
   ```bash
   git clone https://github.com/rihadroshan/keylogger.git
   cd keylogger
   ```

## Usage

**Run the keylogger:**  
   Execute the script:  
   ```bash
   python keylogger.py
   ```

## Log Format

Keystrokes are logged with timestamps like this:  
```
[2025-02-25 14:05:32] H  
[2025-02-25 14:05:33] e  
[2025-02-25 14:05:34] l  
[2025-02-25 14:05:35] l  
[2025-02-25 14:05:36] o  
[2025-02-25 14:05:37] <SPACE>  
[2025-02-25 14:05:38] W  
[2025-02-25 14:05:39] o  
[2025-02-25 14:05:40] r  
[2025-02-25 14:05:41] l  
[2025-02-25 14:05:42] d  
[2025-02-25 14:05:43] <ENTER>  
```
