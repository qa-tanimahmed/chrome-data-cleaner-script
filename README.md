# Chrome Data Cleaner Script

## Overview

This Python script is designed to clear Chrome browser data including history, cache, and cookies. It is particularly useful for manual testing of company products, ensuring that testing environments are clean and free of residual data.

## Features

- **Clears Chrome History**: Deletes the browser's history file.
- **Clears Chrome Cache**: Removes cache files stored by Chrome.
- **Clears Chrome Cookies**: Deletes the cookies file used by Chrome.
- **Handles Different OS**: Works on Windows, macOS, and Linux.
- **Default Paths**: Automatically uses default paths for the Chrome data files.

## Usage

1. **Ensure Chrome is Closed**: The script will prompt if Chrome is currently running. Please close Chrome before running the script.

2. **Run the Script**:
    - Save the script to a file, e.g., `chrome_clear_data.py`.
    - Open a terminal or command prompt.
    - Navigate to the directory where the script is located.
    - Run the script using Python:

      ```bash
      python chrome_clear_data.py
      ```

3. **Single Prompt**:
    - The script will ask: `Do you want to clear Chrome history, cache, and cookies? (yes/no, default is yes):`.
    - Press Enter (default to "yes") to clear all data.
    - Type `no` if you do not wish to clear the data.

## Configuration

- **Default Paths**: The script uses predefined default paths for Chrome's history, cache, and cookies. These paths are automatically detected based on the operating system (Windows, macOS, Linux).

- **Logging**: All actions and errors are logged to `chrome_clear_data.log` for troubleshooting and record-keeping.

## Compatibility

- **Operating Systems**: Windows, macOS, Linux
- **Python Version**: Python 3.x

## Requirements

- Python 3.x
- `psutil` library for process checking

## Installation

To install the required `psutil` library, you can use pip:

```bash
pip install psutil
