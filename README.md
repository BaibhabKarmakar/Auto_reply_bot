# WhatsApp Auto-Reply Bot (Offline – using Ollama + PyAutoGUI)
**An experimental offline auto-reply bot for WhatsApp Web** that:

- Uses screen scraping via PyAutoGUI to select recent chat messages
- Copies the visible chat history to clipboard
- Detects if the last message is **not** from you
- Generates a natural Hinglish reply using **Llama 3.2 (via Ollama)**
- Pastes the reply and sends it automatically

**100% offline after setup** — no cloud APIs, no WhatsApp Business API needed.

**⚠️ Important**: This is **screen-automation-based** → very fragile.  
It depends heavily on:

- Your screen resolution
- WhatsApp Web window size & position
- Browser zoom level (100%)
- No popups / notifications interfering

Use it only for **learning / experimentation** — not for production or important chats.

## Features

- Fully local LLM reply generation (Llama 3.2 3B or 1B)
- Hinglish personality ("Baibhab Karmakar" style)
- Simple last-message detection logic
- Emergency stop: move mouse to top-left corner (PyAutoGUI failsafe)
- Helper script to find exact mouse coordinates

## Current Files

| File            | Purpose                                                                 |
|-----------------|-------------------------------------------------------------------------|
| `bot.py`        | Main script: selects chat → copies → generates reply → pastes & sends   |
| `get_cursor.py` | Infinite loop printing current mouse position (x, y) — use to calibrate |

## Requirements

- Windows / Linux / macOS (tested mainly on Windows)
- Python 3.9+
- [Ollama](https://ollama.com/) installed and running
- Models pulled:
  ```bash
  ollama pull llama3.2:3b
  # or faster but weaker:
  # ollama pull llama3.2:1b
  ```
  WhatsApp Web open in browser (Chrome/Edge recommended), zoomed to 100%
  Chat window maximized or sized consistently

  ## Python packages:
  ``` bash
  pip install pyautogui pyperclip ollama
  ```
  ## How to Use
 1.  Calibrate coordinates (very important!)
  Open get_cursor.py in one terminal:
  ``` bash
  python get_cursor.py
  ```
  Move mouse to these positions and note the printed (x, y):
  1. Chat area top (to start selection)
  2. Chat area bottom
  3. Input box (where you click to focus typing)
  4. Send button (if needed — sometimes Enter is enough)
  5. Initial focus click (if chat needs activation)
  Update the numbers inside bot.py accordingly.
2.  Run the bot : 
  ``` bash
  python bot.py
  ```
  Script waits 5 seconds → gives you time to switch to WhatsApp Web
  It will loop forever, checking every ~4–6 seconds
  Stop it with Ctrl+C or move mouse to top-left corner

## Important Warnings
Brittle automation — if you move browser window, change zoom, get notification popup → bot breaks
Risk of sending wrong messages — test in non-important chat first!
Selection rectangle is fixed vertical line (same x-coordinate) — assumes no horizontal scroll
Last-message detection is very naive → may false-positive or miss messages
Model output sometimes contains extra text → bot pastes raw response

## Possible Improvements (you can try)
Better chat parsing (split by date/time patterns like [DD/MM/YY, HH:MM] - Name:)
Take screenshot + OCR instead of clipboard (more reliable but slower)
Add sleep / random delay to look more human
Filter short / own messages better
Add keyword triggers ("bot on", "bot off")
Save chat logs for context memory

License
MIT License — feel free to copy, modify, learn from it.
Made with curiosity and late-night debugging in West Bengal 🇮🇳
~ Baibhab (Feb 2026)
Happy coding & stay safe with automation experiments!
