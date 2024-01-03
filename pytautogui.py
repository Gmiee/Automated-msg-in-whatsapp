import pyautogui
import time
import subprocess

def open_whatsapp_web():
    try:
        app_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
        subprocess.Popen(app_path)
        time.sleep(5)
        pyautogui.hotkey('ctrl', 'l')
        time.sleep(1)
        pyautogui.write("https://web.whatsapp.com/")
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.alert("Please scan the QR code if you haven't already.")
        time.sleep(2)
        pyautogui.press("enter")
        time.sleep(20)
    except Exception as e:
        print(f"Failed to open Chrome or navigate to WhatsApp Web. Error: {str(e)}")

def perform_actions_after_authentication():
    try:
        print("Performing actions after authentication...")
        time.sleep(2)
        pyautogui.hotkey('alt', 'k')
        time.sleep(1)
        
        # Typing the recipient's name
        recipient_name = pyautogui.prompt("Enter recipient's name: ")
        pyautogui.write(recipient_name)
        time.sleep(3)
        pyautogui.press("enter")
        time.sleep(2)
        
        # Typing the message
        message = "This message is automated and generated in Python."
        pyautogui.write(message)
        pyautogui.press('enter')
        print(f"Message sent to {recipient_name}: {message}")
    except Exception as e:
        print(f"Error occurred while performing actions: {str(e)}")

# Execution starts here
print("Opening WhatsApp Web...")
open_whatsapp_web()

# Perform actions after authentication
perform_actions_after_authentication()


def portfolio():
        pyautogui.hotkey('ctrl', 'l')
        time.sleep(1)
        pyautogui.write("https://jenish.live/")
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.alert("lets Get connected!")
        pyautogui.press('enter')
        
portfolio()