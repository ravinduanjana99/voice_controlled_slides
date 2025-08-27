import json
import queue
import re
import sys
import time

import pyautogui
import sounddevice as sd
from vosk import Model, KaldiRecognizer

# Settings
Model_Path = ".venv/models/vosk-model-small-en-us-0.15"
Sample_Rate = 16000
Blocksize = 8000
Hotword_Required = True
Hotword = "computer"


# These commands are accepted as patterns
Command_Patterns = {
    "NEXT": re.compile(r"\b(next)\b"),
    "PREV": re.compile(r"\b(back)\b"),
    "START": re.compile(r"\b(start)\b"),
    "END": re.compile(r"\b(stop)\b"),
}

# Normalize text to trim adn remove whitespace
def normalize(text: str) -> str:
    return re.sub(r"\s+","", text.strip().lower())

def extract_command(text: str):
    t = normalize(text)

    # Ensure Hotword present if required
    if Hotword_Required:
        if Hotword not in t:
            return None
        t = t.split(Hotword, 1)[1].strip()

    # Check pattern to find matching command in command patterns
    for name, pattern in Command_Patterns.items():
        if pattern.search(t):
            return name

    return None 
    
# Send key press recognized to the os
def send_command(command: str):
    if command == "NEXT":
        pyautogui.press("right") 
        print("[Action] Next >")
    elif command == "PREV":
        pyautogui.press("left")
        print("[Action] Prev <")
    elif command == "START":
        pyautogui.press("f5")
        print("[Action] Start")
    elif command == "END":
        pyautogui.hotkey("esc")
        print("[Action] End Slideshow (ESC)")
        

# Load model 
def main():
    print("Loading Vosk Model...........")
    model = Model(Model_Path)
    rec = KaldiRecognizer(model, Sample_Rate) # Creat e recognizer instance
    q = queue.Queue()
    
    def audio_callback(indata, frames, time, status):
        if status:
            print(status, file=sys.stderr)
        q.put(bytes(indata)) # hold audio passed from callback
        
    with sd.RawInputStream(samplerate=Sample_Rate, blocksize=Blocksize, dtype="int16", channels=1, callback=audio_callback):
        print("Listening.........")
        if Hotword_Required:
            print("Say Hotword + next/prev/start/end")
            
        last_cmd_time = 0.0
        cooldown = 0.7 # this is to wait between commands to avoid clash
        
        # get audio from queue and send to vosk recognizer
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result.get("text", "").strip()
                if not text:
                    continue
                print(f"[HEARD] {text}")
                
                command = extract_command(text)
                now = time.time()
                if command and now - last_cmd_time > cooldown:
                    send_command(command)
                    last_cmd_time = now
                else:
                    pass
                    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")   
                

            