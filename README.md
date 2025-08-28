# 🎤 Voice-Controlled Slide Navigator

A Python-based tool that lets you control presentation slides **hands-free** with your voice.  
It uses [Vosk](https://alphacephei.com/vosk/) for offline speech recognition and [PyAutoGUI](https://pyautogui.readthedocs.io/) to simulate keyboard controls.

This project allows you to start, navigate, and stop a slideshow (PowerPoint, Google Slides, LibreOffice Impress, etc.) using simple spoken commands.

---

## 🚀 Features
- 🎙️ **Offline speech recognition** (no internet required)  
- 🖱️ **Automated keyboard control**  
- 🔑 **Hotword-based activation** (default: `"computer"`)  
- ⏭️ **Supported commands**:
  - `"computer next"` → Next slide  
  - `"computer back"` → Previous slide  
  - `"computer start"` → Start slideshow (`F5`)  
  - `"computer stop"` → End slideshow (`ESC`)  

---

## 🛠️ Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/your-username/voice-slide-navigator.git
   cd voice-slide-navigator

2. **Create a virtual environment**
   python -m venv .venv
   source .venv/bin/activate   # On Linux/macOS
   .venv\Scripts\activate      # On Windows

3. **Install Dependancies**
   Install dependencies
      pip install -r requirements-pinned.txt
   
4. **Model Download**
   Download Vosk Model-.venv/models/vosk-model-small-en-us-0.15 or 
   you can use this command to download the model-
   # For linux or mac
         # Create folder
         mkdir -p .venv/models

         # Download with wget
         wget -O .venv/models/model.zip https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip

         # OR with curl (if wget not installed)
         # curl -L -o .venv/models/model.zip https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip

         # Extract
         unzip .venv/models/model.zip -d .venv/models

         # Clean up
         rm .venv/models/model.zip

   # For windows
         # Create folder
         New-Item -ItemType Directory -Force -Path ".venv\models"

         # Download
         Invoke-WebRequest -Uri "https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip" -OutFile ".venv\models\model.zip"

         # Extract
         Expand-Archive -Path ".venv\models\model.zip" -DestinationPath ".venv\models" -Force

         # Clean up
         Remove-Item ".venv\models\model.zip"


5. **Create a folder name models in .venv**
   -.venv
      -models

6. **Run the programme**
  python voice_slide_controller.py