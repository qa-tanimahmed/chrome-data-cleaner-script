import os
import time
import platform
import psutil
import logging

# Setup logging
logging.basicConfig(filename='chrome_clear_data.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

CONFIG_FILE = 'config.txt'

def is_chrome_running():
    """Check if Chrome is currently running."""
    for process in psutil.process_iter(['name']):
        if process.info['name'] == 'chrome.exe' or process.info['name'] == 'Google Chrome':
            return True
    return False

def get_path(file_type):
    """Get the path to the specified Chrome file type based on the operating system."""
    system = platform.system()
    if system == 'Windows':
        base_path = os.path.expanduser('~') + '/AppData/Local/Google/Chrome/User Data/Default/'
    elif system == 'Darwin':  # macOS
        base_path = os.path.expanduser('~') + '/Library/Application Support/Google/Chrome/Default/'
    elif system == 'Linux':
        base_path = os.path.expanduser('~') + '/.config/google-chrome/Default/'
    else:
        raise OSError("Unsupported operating system")
    
    if file_type == 'history':
        return base_path + 'History'
    elif file_type == 'cache':
        return base_path + 'Cache'
    elif file_type == 'cookies':
        return base_path + 'Cookies'
    else:
        raise ValueError("Unsupported file type")

def clear_chrome_data():
    """Prompt user to clear all three types of Chrome data with default 'yes'."""
    if is_chrome_running():
        print("Chrome is currently running. Please close Chrome before running this script.")
        logging.info("Chrome is currently running. User was prompted to close it.")
        return

    prompt = input("Do you want to clear Chrome history, cache, and cookies? (yes/no, default is yes): ").strip().lower()
    if prompt == '' or prompt == 'yes':
        file_types = ['history', 'cache', 'cookies']
        for file_type in file_types:
            file_path = get_path(file_type)

            attempts = 5
            while attempts > 0:
                try:
                    if os.path.exists(file_path):
                        if file_type == 'cache':
                            # For cache, handle directories differently
                            for root, dirs, files in os.walk(file_path):
                                for file in files:
                                    os.remove(os.path.join(root, file))
                        else:
                            os.remove(file_path)
                        logging.info(f"Chrome {file_type} cleared.")
                        print(f"Chrome {file_type} cleared.")
                        break
                    else:
                        logging.info(f"No Chrome {file_type} file found.")
                        print(f"No Chrome {file_type} file found.")
                        break
                except PermissionError as e:
                    logging.warning(f"File is currently in use. Retrying... ({attempts-1} attempts left)")
                    print(f"File is currently in use. Retrying... ({attempts-1} attempts left)")
                    time.sleep(5)
                    attempts -= 1
                except Exception as e:
                    logging.error(f"An error occurred: {e}")
                    print(f"An error occurred: {e}")
                    break
    else:
        print("No data will be cleared.")
        logging.info("User chose not to clear data.")

if __name__ == "__main__":
    clear_chrome_data()
    input("Press Enter to exit...")  # Pause so you can see any messages
