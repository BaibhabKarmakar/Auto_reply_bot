import pyautogui
import time
import pyperclip   # ← used to safely read clipboard
from ollama import chat     # offline Models I am currently using llama3.2:1b (Super fast for quick answering)
from ollama import ChatResponse

def is_last_message_not_from_CodeWithMeBK(chat_log , sender_name = "CodeWithMeBK"):
    messages = chat_log.strip().split("/2026]")[-1]
    if not(sender_name) in messages:
        return True
    return False




# Safety settings
pyautogui.FAILSAFE = True       # ← move mouse to top-left corner = emergency stop
pyautogui.PAUSE = 0.25          # small delay between actions

print("Script starts in 5 seconds. Move mouse to TOP-LEFT corner to abort!")
time.sleep(5)
pyautogui.click(1160, 1054)
time.sleep(0.6)                 # give time for focus / caret to appear

while True:

    pyautogui.moveTo(1170 , 160 , duration=0.4)
    pyautogui.mouseDown(button='left')
    pyautogui.moveTo(1170 , 970, duration=1.1)   # ← adjust duration if selection flickers
    pyautogui.mouseUp(button='left')
    time.sleep(0.4)

    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(1204 , 945)
    time.sleep(0.5)                 # important: give time for clipboard to update

    # Get the copied text into a variable
    chat_history = pyperclip.paste()

    print(chat_history)
    print(is_last_message_not_from_CodeWithMeBK(chat_history))
    if is_last_message_not_from_CodeWithMeBK(chat_history):

        # You can now work with the variable, for example:
        if chat_history.strip():
            print(f"Length of selected text: {len(chat_history)} characters")
            # first_line = chat_history.splitlines()[0]
            # print("First line:", first_line)
        else:
            print("Warning: clipboard is empty → selection or copy may have failed")


        response : ChatResponse = chat(model = "llama3.2:3b" , messages = [
                {
                    "role" : "System",
                    "content" : "You are a perosn named 'Baibhab Karmakar' who speaks hindi , bengali as well as  english . You are from India and is a coder . You analyse the chat history and respond like baibhab .just reply with them in hinglish (I mean the mixture of hindi and english) . your text will be the the reply of the last chat the other person is asking to you . Ouput should be message only. "
                },
                {
                    "role" : "User",
                    "content" : chat_history
                },
            ])
        response = response['message']['content']

        pyperclip.copy(response)
        pyautogui.click(1170 , 1000)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)

        pyautogui.press('enter')