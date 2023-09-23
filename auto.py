import os
import subprocess
import time
import pyautogui

# Set the path to the HTML testcases directory
testcases_dir = '/home/sick/fuzzing/fuzzer/asan-linux-release-1192588/output'

# Set the path to the Chrome ASAN executable
chrome_asan_path = '/home/sick/fuzzing/fuzzer/asan-linux-release-1192588/chrome'

# List all HTML files in the testcases directory
html_files = [f for f in os.listdir(testcases_dir) if f.endswith('.html')]

# Start Chrome ASAN in a new terminal
chrome_cmd = f'x-terminal-emulator -e {chrome_asan_path}'

# Execute the Chrome ASAN command in the terminal
chrome_process = subprocess.Popen(chrome_cmd, shell=True)

# Wait for Chrome to open
time.sleep(5)

# Loop through the HTML files and open them in new tabs within the same Chrome instance
for html_file in html_files:
    html_file_path = os.path.join(testcases_dir, html_file)
    
    # Simulate the keyboard shortcut to open a new tab (Ctrl+T)
    pyautogui.hotkey('ctrl', 't')
    
    # Wait for a moment to allow the new tab to open
    time.sleep(2)
    
    # Simulate typing the URL and pressing Enter to load the HTML testcase
    pyautogui.typewrite(f'file://{html_file_path}')
    pyautogui.press('enter')
    
    # Wait for 10 seconds (or adjust as needed)
    time.sleep(10)
    
    # Simulate the keyboard shortcut to close the current tab (Ctrl+W)
    pyautogui.hotkey('ctrl', 'w')

# Close the Chrome ASAN browser when all testcases are done
chrome_process.terminate()
