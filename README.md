## Features

- **Keystroke Logging**: Captures and logs keystrokes, including special keys like Enter and Backspace.
- **Console Hiding**: Hides the console window to avoid disrupting the user's experience.
- **Automatic Package Installation**: Installs necessary packages if they are not already installed.

## Requirements

- Python 3.x
- `pynput`
- `pywin32`

## Installation

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/rihadroshan/keylogger.git
    cd keylogger
    ```

2. **Install Required Packages**:

    The script automatically installs the necessary packages if they are not already installed. You can also manually install them using pip:

    ```bash
    pip install -r requirements.txt
    
    ```

## Usage

1. **Modify the Script**:

    Edit the `keylog_file` path in the script to specify where the keystrokes will be logged. Ensure the path is accessible and writable by the script.

    ```python
    keylog_file = r'C:\path\to\your\keylog.txt'
    ```

2. **Run the Script**:

    Execute the script using Python:

    ```bash
    python3 keylogger.py
    ```

    The script will log keystrokes to the specified file and hide the console window.

## Notes

- **Ethical Use**: This script is for educational purposes only. Unauthorized use of keyloggers is illegal and unethical. Always obtain explicit consent before monitoring keyboard activity.
- **Security**: Be cautious about where and how you use this script. Protect sensitive information and ensure it is used responsibly.
