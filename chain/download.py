import pyautogui
import time
import subprocess

# Step 1: Click on (496,83)
pyautogui.click(496, 83)
time.sleep(1)

# Step 2: Write the URL and press Enter
url = "https://chainide.com/s/ethereum/a34641e86fbb45e696da6f908e95f21e"
pyautogui.write(url)
time.sleep(0.5)
pyautogui.press("enter")
time.sleep(1)

# Step 3: Run sandbox.py
subprocess.run(["python3", "sandbox.py"])
time.sleep(1)

# Step 4: Write netstat command and press Enter
pyautogui.write("netstat -tuln | grep 8070")
time.sleep(0.5)
pyautogui.press("enter")
time.sleep(4)

# Step 5: Detect listen_button.png
image_path = "listen_button.png"
confidence_level = 0.8  # Adjust as needed

button_location = None  # Initialize variable

try:
    button_location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence_level, grayscale=True)
except pyautogui.ImageNotFoundException:
    print("Image not found. Proceeding with the alternative steps.")

# If button is detected
if button_location:
    pyautogui.click(291, 42)
    time.sleep(1)
    pyautogui.click(251, 40)
    time.sleep(1)
else:
    # If button is not detected, execute the alternative steps
    pyautogui.click(604, 505)
    time.sleep(0.5)

    command = "sudo apt -y update && sudo apt -y install nano tmux redis-server python3 python3-pip && pip install redis nest_asyncio fastapi uvicorn flask python-multipart"
    pyautogui.write(command)
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(1.5)
    # Run rooto.py
    subprocess.run(["python3", "rooot.py"])
    time.sleep(0.7)

    # Open tmux
    pyautogui.write("tmux")
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(1.5)

    # Start Redis server
    pyautogui.write("redis-server")
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(4)

    # Exit tmux session with Ctrl+B then D
    pyautogui.hotkey("ctrl", "b")
    pyautogui.press("d")
    time.sleep(1)

    # Run server.py
    pyautogui.write("python3 server.py")
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(4)

    # Click on (291,42) then (251,40)
    pyautogui.click(291, 42)
    time.sleep(1)
    pyautogui.click(251, 40)
    time.sleep(1)
