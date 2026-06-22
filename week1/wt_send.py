import pyautogui
import time

def send_whatsapp_messages(message: str, count: int):
    print(f"Starting in 5 seconds... Switch to WhatsApp Desktop and open the target chat!")
    time.sleep(5)  # Give you time to switch to WhatsApp

    for i in range(1, count + 1):
        # Click on the message input box (bottom center of the screen usually)
        # Adjust coordinates if needed — or just make sure WhatsApp is in focus
        # Click on message input field
        # pyautogui.click()  # clicks wherever your cursor is — position it on the input box
        # time.sleep(0.005)

        # Type the message
        pyautogui.typewrite(f"{message}", interval=0.5)

        # Press Enter to send
        pyautogui.press('enter')



if __name__ == "__main__":
    # ── CONFIGURE THESE ──────────────────────────────
    MESSAGE = "A__"
    COUNT   = 500  # Number of messages to send
    # ─────────────────────────────────────────────────

    send_whatsapp_messages(MESSAGE, COUNT)